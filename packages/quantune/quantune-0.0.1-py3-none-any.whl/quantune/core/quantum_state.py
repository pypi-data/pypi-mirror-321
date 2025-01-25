'''import numpy as np
from .tools import measure

# Base classes and utilities
#This will be put on hold for Some time

class QuantumState:
    """
    A class representing a quantum state (vector).
    """

    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.state = np.zeros(2**num_qubits, dtype=np.complex128)
        self.state[0] = 1.0  # Start in |0...0> state

    def apply_unitary(self, unitary: np.ndarray):
        """
        Apply a unitary transformation to the quantum state.
        """
        if unitary.shape != (2**self.num_qubits, 2**self.num_qubits):
            raise ValueError("Unitary matrix dimension do not match.")
        self.state = np.dot(unitary, self.state)

    def get_state(self) -> np.ndarray:
        return self.state

    def measure(self) -> str:
        """
        Measure the quantum state, collapsing it to one basis state.
        """
        return measure(self.state)
'''
