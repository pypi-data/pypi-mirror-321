# Copyright 2023-2024 Qualition Computing LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://github.com/Qualition/quick/blob/main/LICENSE
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" Shende's Shannon decomposition for preparing quantum unitary operators
using multiplexed RY and RZ gates.
"""

from __future__ import annotations

__all__ = ["ShannonDecomposition"]

from collections.abc import Sequence
import numpy as np
from numpy.typing import NDArray
import scipy.linalg # type: ignore
from typing import SupportsIndex, TYPE_CHECKING

import quick
if TYPE_CHECKING:
    from quick.circuit import Circuit
from quick.circuit.circuit_utils import decompose_multiplexor_rotations
from quick.predicates import is_hermitian_matrix
from quick.primitives import Operator
from quick.synthesis.unitarypreparation import UnitaryPreparation

# Constants
QUBIT_KEYS = frozenset([
    "qubit_index", "control_index", "target_index"
])


class ShannonDecomposition(UnitaryPreparation):
    """ `quick.ShannonDecomposition` is the class for preparing quantum operators
    using Shannon decomposition.

    Notes
    -----
    Shende's Shannon decomposition uses multiplexed RY and RZ gates to prepare the unitary
    operator. This method scales exponentially with the number of qubits in terms of circuit
    depth.

    ```
       ┌───┐               ┌───┐     ┌───┐     ┌───┐
      ─┤   ├─       ───────┤ Rz├─────┤ Ry├─────┤ Rz├─────
       │   │    ≃     ┌───┐└─┬─┘┌───┐└─┬─┘┌───┐└─┬─┘┌───┐
     /─┤   ├─       /─┤   ├──□──┤   ├──□──┤   ├──□──┤   ├
       └───┘          └───┘     └───┘     └───┘     └───┘
    ```

    The number of CX gates generated with the decomposition without optimizations is,

    .. math::

        \frac{9}{16} 4^n - \frac{3}{2} 2^n

    With A.1 optimization the CX count is reduced by,

    .. math::

        \frac{1}{3} 4^{n - 2} - 1.

    With A.2 optimization the CX count is reduced by,

    .. math::

        4^{n-2} - 1.

    Both A.1 and A.2 optimizations are applied by default.

    For more information on Shannon decomposition:
    [1] Shende, Bullock, Markov.
    Synthesis of Quantum Logic Circuits (2004)
    https://arxiv.org/abs/quant-ph/0406176

    Parameters
    ----------
    `output_framework` : type[quick.circuit.Circuit]
        The quantum circuit framework.

    Attributes
    ----------
    `output_framework` : type[quick.circuit.Circuit]
        The quantum circuit framework.

    Raises
    ------
    TypeError
        - If the output framework is not a subclass of `quick.circuit.Circuit`.
    """
    def __init__(
            self,
            output_framework: type[Circuit]
        ) -> None:

        super().__init__(output_framework)

        self.one_qubit_decomposition = quick.synthesis.gate_decompositions.OneQubitDecomposition(output_framework)
        self.two_qubit_decomposition = quick.synthesis.gate_decompositions.TwoQubitDecomposition(output_framework)

    def apply_unitary(
            self,
            circuit: Circuit,
            unitary: NDArray[np.complex128] | Operator,
            qubit_indices: int | Sequence[int]
        ) -> Circuit:

        if not isinstance(unitary, (np.ndarray, Operator)):
            try:
                unitary = np.array(unitary).astype(complex)
            except (ValueError, TypeError):
                raise TypeError(
                    "The operator must be a numpy array or an Operator object. "
                    f"Received {type(unitary)} instead."
                )

        if isinstance(unitary, np.ndarray):
            unitary = Operator(unitary)

        if isinstance(qubit_indices, SupportsIndex):
            qubit_indices = [qubit_indices]

        if not all(isinstance(qubit_index, SupportsIndex) for qubit_index in qubit_indices):
            raise TypeError("All qubit indices must be integers.")

        if not len(qubit_indices) == unitary.num_qubits:
            raise ValueError("The number of qubit indices must match the number of qubits in the unitary.")

        a2_qsd_blocks: list[list[int]] = []

        def quantum_shannon_decomposition(
                circuit: Circuit,
                qubit_indices: list[int],
                unitary: NDArray[np.complex128],
                recursion_depth: int=0
            ) -> None:
            """ Decompose n-qubit unitary into CX/RY/RZ/CX gates, preserving global phase.

            Notes
            -----
            Using cosine-sine decomposition, the unitary matrix is decomposed into a series of
            single-qubit rotations and CX gates. The most significant qubit is then decomposed
            into a series of RY rotations and CX gates, and the process is repeated recursively
            until the unitary is fully decomposed.

            ```
              ┌───┐               ┌───┐
            ──┤   ├──      ────□──┤ Ry├──□───
              │ U │    =     ┌─┴─┐└─┬─┘┌─┴─┐
            /─┤   ├──      /─┤ U ├──□──┤ V ├─
              └───┘          └───┘     └───┘
            ```

            Parameters
            ----------
            `circuit` : quick.circuit.Circuit
                Quantum circuit to append operations to.
            `qubit_indices` : list[int]
                The qubits to apply the unitary to.
            `unitary` : NDArray[np.complex128]
                N-qubit unitary matrix to be decomposed.
            `recursion_depth` : int, optional, default=0
                The current recursion depth.

            Raises
            ------
            ValueError
                - If the u matrix is non-unitary
                - If the u matrix is not of shape (2^n,2^n)
            """
            dim = unitary.shape[0]

            # Explicit decomposition for one and two qubit unitaries
            # This is the base case for the recursion
            if dim == 2:
                self.one_qubit_decomposition.apply_unitary(circuit, unitary, qubit_indices)
                return

            elif dim == 4:
                current_index = len(circuit.circuit_log)
                self.two_qubit_decomposition.apply_unitary(circuit, unitary, qubit_indices)

                # Store the block for A.2 optimization
                if recursion_depth > 0:
                    a2_qsd_blocks.append([current_index, len(circuit.circuit_log)])

                return

            # Perform cosine-sine decomposition per Theorem 10
            (u1, u2), theta, (v1, v2) = scipy.linalg.cossin(unitary, separate=True, p=dim//2, q=dim//2)

            # Left multiplexed circuit
            demultiplexor(circuit, qubit_indices, v1, v2, recursion_depth)

            # Perform A.1 optimization from Shende et al.
            # This optimization reduces the number of CX gates by 1/3 * 4^(n-2) - 1
            num_angles = len(theta)

            # The multiplexed RY gate is replaced by its equivalent CZ-RY gate
            # and merge final CZ gate with the neighboring right-side generic
            # multiplexer to apply A.1 optimization
            # This removes one CX gate at each step of the recursion
            ucry_to_cz_ry(circuit, qubit_indices[:-1], qubit_indices[-1], (2 * theta).tolist())
            u2[:, num_angles // 2:] = np.negative(u2[:, num_angles // 2:])

            # Right multiplexed circuit
            demultiplexor(circuit, qubit_indices, u1, u2, recursion_depth)

            # Once the recursion reaches the base case, apply the A.2 optimization
            # to reduce the number of CX gates by 4^(n-2) - 1
            if recursion_depth == 0:
                a2_optimization(circuit, a2_qsd_blocks)

        def demultiplexor(
                circuit: Circuit,
                demux_qubits: list[int],
                unitary_1: NDArray[np.complex128],
                unitary_2: NDArray[np.complex128],
                recursion_depth: int=0
            ) -> None:
            """ Decompose a multiplexor defined by a pair of unitary matrices operating on
            the same subspace per Theorem 12.

            That is, decompose

            ```
              ctrl     ────□────
                        ┌──┴──┐
              target  /─┤     ├─
                        └─────┘
            ```

            represented by the block diagonal matrix

            ```
                ┏         ┓
                ┃ U1      ┃
                ┃      U2 ┃
                ┗         ┛
            ```

            to

            ```
                             ┌───┐
              ctrl    ───────┤ Rz├──────
                        ┌───┐└─┬─┘┌───┐
              target  /─┤ W ├──□──┤ V ├─
                        └───┘     └───┘
            ```

            by means of simultaneous unitary diagonalization.

            Parameters
            ----------
            `circuit` : quick.circuit.Circuit
                Quantum circuit to append operations to.
            `demux_qubits` : list[int]
                Subset of total qubits involved in this unitary gate.
            `unitary_1` : NDArray[np.complex128]
                Upper-left quadrant of total unitary to be decomposed (see diagram).
            `unitary_2` : NDArray[np.complex128]
                Lower-right quadrant of total unitary to be decomposed (see diagram).
            `recursion_depth` : int, optional, default=0
                The current recursion depth.
            """
            # Compute the product of `unitary_1` and the conjugate transpose of `unitary_2`
            u = unitary_1 @ unitary_2.conj().T

            # Perform eigenvalue decomposition to find the eigenvalues and eigenvectors of u
            # This step is crucial because it allows us to express the unitary transformation
            # in terms of its eigenvalues and eigenvectors, which simplifies further calculations
            if is_hermitian_matrix(u):
                eigenvalues, eigenvectors = scipy.linalg.eigh(u)
            else:
                # If the matrix is not Hermitian, use the Schur decomposition
                # to compute the eigenvalues and eigenvectors
                eigenvalues, eigenvectors = scipy.linalg.schur(u, output="complex") # type: ignore
                eigenvalues = eigenvalues.diagonal()

            # Take the square root of the eigenvalues to obtain the singular values
            # This is necessary because the singular values provide a more convenient form
            # for constructing the diagonal matrix D, which is used in the final decomposition
            # We need to use `np.emath.sqrt` to handle negative eigenvalues
            eigenvalues_sqrt = np.emath.sqrt(eigenvalues)

            # Create a diagonal matrix D from the singular values
            # The diagonal matrix D is used to scale the eigenvectors appropriately in the final step
            diagonal = np.diag(eigenvalues_sqrt)

            # Compute the matrix W using D, the conjugate transpose of V, and `unitary_2`
            # This step combines the scaled eigenvectors with the original unitary matrix to
            # achieve the desired decomposition
            W = diagonal @ eigenvectors.conj().T @ unitary_2

            # Apply the left gate
            quantum_shannon_decomposition(circuit, demux_qubits[:-1], W, recursion_depth + 1)

            # Apply multiplexed RZ gate
            angles = (2 * np.angle(
                np.conj(eigenvalues_sqrt)
            )).tolist()

            circuit.UCRZ(angles, demux_qubits[:-1], demux_qubits[-1])

            # Apply the right gate
            quantum_shannon_decomposition(circuit, demux_qubits[:-1], eigenvectors.astype(complex), recursion_depth + 1)

        def ucry_to_cz_ry(
                circuit: Circuit,
                control_indices: int | list[int],
                target_index: int,
                angles: NDArray[np.float64]
            ) -> None:
            """ Get the multiplexed RY gate in terms of CZ-RY. This
            is used in the A.1 optimization.

            Notes
            -----
            As the initial controlled-Z gate is diagonal, it may be absorbed into the
            neighboring generic multiplexor. This saves one CX gate at each step of the
            recursion, for the total savings of (4^(n-l) -1)/3 CX gates.

            Parameters
            ----------
            `circuit` : quick.circuit.Circuit
                Quantum circuit to append operations to.
            `control_indices` : int | list[int]
                List of control qubits for the CZ gate.
            `target_index` : int
                Target qubit for the CZ gate.
            `angles` : NDArray[np.float64]
                List of angles for the RY gates.
            """
            num_angles = len(angles)

            if isinstance(control_indices, int):
                control_indices = [control_indices]

            # If there are no control qubits, apply the RY gate directly
            # to the target qubit
            if not control_indices:
                circuit.RY(angles[0], target_index)
                return

            # Calculate rotation angles for a multiplexed Pauli Rotation gate
            # with a CX gate at the end of the circuit
            angles = decompose_multiplexor_rotations(angles, 0, len(angles), False)

            for i, angle in enumerate(angles):
                circuit.RY(angle, target_index)

                if not i == len(angles) - 1:
                    binary_rep = np.binary_repr(i + 1)
                    control_index = len(binary_rep) - len(binary_rep.rstrip("0"))
                else:
                    # Handle special case for last angle
                    control_index = len(control_indices) - 1

                # Leave off last CZ for merging with neighboring multiplexor as part
                # of A.1 optimization
                if i < num_angles - 1:
                    circuit.CZ(control_indices[control_index], target_index)

        def a2_optimization(
                circuit: Circuit,
                a2_qsd_blocks: list[list[int]]
            ) -> None:
            """ Extract diagonals to improve decomposition of two-qubit gates. This
            is used in the A.2 optimization.

            Notes
            -----
            We use Theorem 14 to decompose the rightmost two-qubit operator; migrate
            the diagonal through the select bits of the multiplexor to the left, and
            join it with the two-qubit operator on the other side.

            Now we decompose this operator, and continue the process. Since we save
            one CX in the implementation of every two-qubit gate but the last, we
            improve the l = 2, c_l = 3 count by 4^(n - 2) - 1 gates.

            Parameters
            ----------
            `circuit` : quick.circuit.Circuit
                Quantum circuit to append operations to.
            `a2_qsd_blocks` : list[list[int]]
                List of blocks to apply A.2 optimization to.
            """
            # If there are no blocks, or only one block which means
            # no neighbors to merge diagonal into, then return
            if len(a2_qsd_blocks) < 2:
                return

            # Break apart the circuit into the blocks that need to be changed
            # and the blocks that will remain the same
            qsd_blocks: list[list[dict]] = []
            circuit_blocks: list[list[dict]] = []

            circuit_blocks.append(circuit.circuit_log[:a2_qsd_blocks[0][0]])

            for block_index, block in enumerate(a2_qsd_blocks[:-1]):
                qsd_blocks.append(circuit.circuit_log[block[0]:block[1]])
                circuit_blocks.append(circuit.circuit_log[block[1]:a2_qsd_blocks[block_index + 1][0]])

            qsd_blocks.append(circuit.circuit_log[a2_qsd_blocks[-1][0]:a2_qsd_blocks[-1][1]])
            circuit_blocks.append(circuit.circuit_log[a2_qsd_blocks[-1][1]:])

            # Extract the blocks from the circuit
            for block_index in range(len(qsd_blocks) - 1):
                circuit_1 = self.output_framework(2)
                circuit_2 = self.output_framework(2)

                circuit_1.circuit_log = qsd_blocks[block_index]
                circuit_2.circuit_log = qsd_blocks[block_index + 1]

                # Update the circuit to reconstruct the circuit from the modified circuit log
                # As mentioned, we need to map the qubits to 0 and 1 to extract the 4x4 unitaries
                if block_index == 0:
                    for operation in circuit_1.circuit_log:
                        for key in set(operation.keys()).intersection(QUBIT_KEYS):
                            operation[key] = 0 if operation[key] == qubit_indices[0] else 1

                for operation in circuit_2.circuit_log:
                    for key in set(operation.keys()).intersection(QUBIT_KEYS):
                        operation[key] = 0 if operation[key] == qubit_indices[0] else 1

                circuit_1.update()
                circuit_2.update()

                unitary_1 = circuit_1.get_unitary()
                unitary_2 = circuit_2.get_unitary()

                # Perform diagonalization of the unitary blocks
                circuit_1, diagonal = self.two_qubit_decomposition.apply_unitary_up_to_diagonal(
                    self.output_framework(2),
                    unitary_1,
                    [0, 1]
                )
                circuit_2 = self.two_qubit_decomposition.prepare_unitary(unitary_2 @ diagonal)

                # Update the blocks
                qsd_blocks[block_index] = circuit_1.circuit_log
                qsd_blocks[block_index + 1] = circuit_2.circuit_log

            # Undo the qubit mapping
            for block in qsd_blocks: # type: ignore
                for operation in block: # type: ignore
                    for key in set(operation.keys()).intersection(QUBIT_KEYS):
                        operation[key] = qubit_indices[0] if operation[key] == 0 else qubit_indices[1]

            # Reconstruct the circuit with the modified blocks in alternating order
            circuit.reset()

            circuit.circuit_log.extend(circuit_blocks.pop(0))

            for qsd_block, circuit_block in zip(qsd_blocks, circuit_blocks):
                circuit.circuit_log.extend(qsd_block)
                circuit.circuit_log.extend(circuit_block)

            # Update the circuit to reconstruct the circuit from the modified circuit log
            circuit.update()

        # Apply the Shannon decomposition to the circuit
        quantum_shannon_decomposition(circuit, qubit_indices, unitary.data, recursion_depth=0) # type: ignore

        return circuit