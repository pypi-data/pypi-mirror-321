from quantune import QuantumCircuit
import numpy as np
from quantune.core.quantum_gate.gates import hadamard

# Initialize a 3-qubit circuit
num_qubits = 3
qc = QuantumCircuit(num_qubits)

# Add a Hadamard gate to the first qubit (qubit 0)
qc.add_gate(hadamard(), [0], "H")

# Execute the circuit
qc.execute()

# Define the expected state after applying the Hadamard gate to qubit 0
expected_state = np.zeros(2**num_qubits, dtype=np.complex128)
expected_state[0] = 1 / np.sqrt(2)  # |000>
expected_state[4] = 1 / np.sqrt(2)  # |100>

# Get the actual state from the QuantumRegister
actual_state = qc.register.get_state()

# Print results for debugging
print(f"Expected state: {expected_state}")
print(f"Actual state: {actual_state}")

# Assert that the actual state matches the expected state
assert np.allclose(
    actual_state, expected_state
), f"Test failed! Expected state: {expected_state}, Actual state: {actual_state}"

print("Test passed: Single Hadamard gate")
