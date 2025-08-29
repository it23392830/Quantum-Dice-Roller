from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def quantum_random_number():
    # 3 qubits to cover 0-7
    qc = QuantumCircuit(3, 3)
    qc.h([0, 1, 2])          # Put qubits in superposition
    qc.measure([0, 1, 2], [0, 1, 2])

    # Use AerSimulator
    simulator = AerSimulator()
    job = simulator.run(qc, shots=1)
    result = job.result()
    counts = result.get_counts(qc)
    
    random_bin = list(counts.keys())[0]
    random_num = int(random_bin, 2)
    return random_num

def quantum_dice_roll():
    while True:
        num = quantum_random_number()
        if num < 6:  # Only 0-5
            return num + 1

if __name__ == "__main__":
    for i in range(5):
        print("Quantum dice roll:", quantum_dice_roll())

