'''from typing import Union
from numpy import arange, log2, ndarray, random
from ..quantum_circuit import QuantumCircuit
from .base import convert_state
from .probability import probability


def measure(quantumstate: Union[ndarray, QuantumCircuit]) -> str:
    """Outputs the measure of a quantum circuit state.
    ```
    from qcpy import quantumcircuit, measure
    measure(quantumcircuit(qubits = 2))
    ```
    Returns:
        NDArray: Amplitude array from given state.
    """
    state = convert_state(quantumstate)
    size = int(log2(state.size))
    probabilities = probability(state, round=None)
    measured_index = random.choice(arange(len(state)), p=probabilities)
    return bin(measured_index)[2:].zfill(size)
'''
