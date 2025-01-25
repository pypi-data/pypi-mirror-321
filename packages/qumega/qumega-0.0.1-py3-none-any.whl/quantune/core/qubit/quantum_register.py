import numpy as np
from .qubit import Qubits


class QuantumRegister:
    """
    A class representing a quantum register with an associated quantum state.

    Attributes:
        num_qubits (int): Number of qubits in the register.
        state (np.ndarray): Complex state vector representing the quantum state.
        qubits (list[Qubit]): List of Qubit objects representing individual qubits.
    """

    def __init__(self, num_qubits: int):
        if not isinstance(num_qubits, int) or num_qubits <= 0:
            raise ValueError("num_qubits must be a positive integer.")
        self.num_qubits = num_qubits
        self.state = np.zeros(2**num_qubits, dtype=np.complex128)  # Use NumPy array
        self.state[0] = 1.0  # Initialize to |0...0>
        self.qubits = [Qubits(index=i) for i in range(num_qubits)]

    def get_state(self, validate: bool = False) -> np.ndarray:
        """
        Get the quantum state of the register.

        Args:
            validate (bool): Whether to validate the normalization of the state.

        Returns:
            np.ndarray: Current state vector.

        Raises:
            ValueError: If validate is True and the state vector is not normalized.
        """
        if validate and not np.isclose(np.sum(np.abs(self.state) ** 2), 1.0, atol=1e-6):
            raise ValueError("State vector is not normalized.")
        return self.state

    def set_state(self, new_state: np.ndarray):
        """
        Set the quantum state of the register.
        """
        if not isinstance(new_state, np.ndarray) or new_state.dtype != np.complex128:
            raise TypeError("new_state must be a NumPy array with dtype=np.complex128.")

        # Validate size and normalization
        if len(new_state) != 2**self.num_qubits:
            raise ValueError(
                f"State vector size must be {2**self.num_qubits}, but got {len(new_state)}."
            )
        if not np.isclose(np.sum(np.abs(new_state) ** 2), 1.0, atol=1e-6):
            raise ValueError("State vector must be normalized.")

        self.state = new_state

    def reset(self):
        self.state = np.zeros(2**self.num_qubits, dtype=np.complex128)
        self.state[0] = 1.0  # Normalize
