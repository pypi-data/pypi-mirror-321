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

__all__ = [
    "OneQubitDecomposition",
    "TwoQubitDecomposition"
]

from quick.synthesis.gate_decompositions.one_qubit_decomposition import OneQubitDecomposition
from quick.synthesis.gate_decompositions.two_qubit_decomposition.two_qubit_decomposition import TwoQubitDecomposition