from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

# Create the quantum circuit
qc = QuantumCircuit(3, 3)
qc.h([0, 1, 2])             # Hadamard gates
qc.measure([0, 1, 2], [0, 1, 2])  # Measure qubits

# Draw and save the circuit diagram
fig = qc.draw(output='mpl')
fig.savefig("quantum_dice_circuit.png")
print("Circuit diagram saved as quantum_dice_circuit.png")
