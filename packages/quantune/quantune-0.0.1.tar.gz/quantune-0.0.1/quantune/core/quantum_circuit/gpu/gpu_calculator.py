import cupy as cp
from ..interface import CalculatorInterface


class GpuCalculator(CalculatorInterface):
    def __init__(self, qubits, prep="z"):
        self.qubits = qubits
        self.prep = prep

    def initialize_state(self):
        state = cp.zeros(2**self.qubits, dtype=cp.complex128)
        state[0] = 1  # Initialize in the |0...0> state
        return state

    def gate_apply(self, gate, target):
        full_gate = self._create_full_gate(gate, target)
        self.state = cp.dot(full_gate, self.state)

    def _create_full_gate(self, gate, target):
        num_qubits = self.qubits
        identity = cp.eye(2, dtype=cp.complex128)
        full_gate = cp.array([[1]], dtype=cp.complex128)

        for i in range(num_qubits):
            if i in target:
                full_gate = cp.kron(full_gate, gate)
            else:
                full_gate = cp.kron(full_gate, identity)

        return full_gate

    def measure_state(self):
        probabilities = cp.abs(self.state) ** 2
        return cp.asnumpy(probabilities)
