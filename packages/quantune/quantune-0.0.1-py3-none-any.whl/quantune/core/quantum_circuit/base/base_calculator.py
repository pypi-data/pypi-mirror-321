import numpy as np
from ..interface import CalculatorInterface
from ...qubit import QuantumRegister


class BaseCalculator(CalculatorInterface):
    def __init__(self, num_qubits, prep="z"):
        self.num_qubits = num_qubits
        self.register = QuantumRegister(num_qubits)
        self.prep = prep
        self.state = self.initialize_state()

    def initialize_state(self):
        state = np.zeros(2**self.num_qubits, dtype=np.complex128)
        state[0] = 1  # Initialize in the |0...0> state
        return state

    def gate_apply(self, gate: np.ndarray, target: list[int]):
        """
        Apply a quantum gate to the state vector.

        Args:
            gate (np.ndarray): The gate matrix to apply.
            target (list[int]): The target qubits for the gate.
        """
        if not all(0 <= q < self.num_qubits for q in target):
            raise ValueError(
                f"Target qubits {target} are out of range for this system."
            )
        # Verify state vector size
        if self.state.shape[0] != 2**self.num_qubits:
            raise ValueError(
                f"State vector size mismatch: expected {2**self.num_qubits}, got {self.state.shape[0]}"
            )
        full_gate = self._create_full_gate(gate, target)
        # Ensure the gate matches the state vector
        if full_gate.shape[0] != self.state.shape[0]:
            raise ValueError(
                f"Expanded gate size {full_gate.shape} does not match state vector size {self.state.shape}"
            )
        # Update the state by applying the full gate matrix
        self.state = np.dot(full_gate, self.state)
        self.state /= np.linalg.norm(self.state)

    def _create_full_gate(self, gate: np.ndarray, target: list[int]) -> np.ndarray:
        """
        Expand a gate matrix to act on the entire quantum system.

        Args:
            gate (np.ndarray): The gate matrix.
            target (list[int]): The indices of qubits the gate acts on.

        Returns:
            np.ndarray: The full-system gate matrix.
        """
        num_qubits = self.num_qubits
        identity = np.eye(2, dtype=np.complex128)

        # Start with a 1x1 matrix
        full_gate = 1
        for i in range(num_qubits):
            if i in target:
                full_gate = np.kron(
                    full_gate, gate
                )  # Apply the gate to targeted qubits
            else:
                full_gate = np.kron(full_gate, identity)  # Identity for other qubits
        return full_gate

    def measure_state(self):
        return np.abs(self.state) ** 2
