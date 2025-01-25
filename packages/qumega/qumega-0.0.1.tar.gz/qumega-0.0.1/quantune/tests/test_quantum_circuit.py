import pytest
import numpy as np
from quantune import QuantumCircuit
from quantune.core.quantum_gate.gates import hadamard, paulix, cnot


@pytest.fixture
def qc_three_qubits():
    return QuantumCircuit(3)


@pytest.fixture
def qc_two_qubits():
    return QuantumCircuit(2)


def test_single_hadamard(qc_three_qubits):
    # Apply Hadamard to the first qubit
    qc_three_qubits.add_gate(hadamard(), [0], "H")
    qc_three_qubits.execute()

    # Expected state: Hadamard creates superposition on qubit 0
    expected_state = np.zeros(2**qc_three_qubits.num_qubits, dtype=np.complex128)
    expected_state[0] = 1 / np.sqrt(2)  # |000>
    expected_state[4] = 1 / np.sqrt(2)  # |100>

    assert np.allclose(qc_three_qubits.register.get_state(), expected_state)
    assert np.isclose(np.sum(np.abs(qc_three_qubits.register.get_state()) ** 2), 1.0)


def test_multiple_hadamards(qc_two_qubits):
    # Apply Hadamard to both qubits
    qc_two_qubits.add_gate(hadamard(), [0], "H")
    qc_two_qubits.add_gate(hadamard(), [1], "H")
    qc_two_qubits.execute()

    # Expected state: Equal superposition of all states
    expected_state = np.array([1, 1, 1, 1], dtype=np.complex128) / 2

    assert np.allclose(qc_two_qubits.register.get_state(), expected_state)
    assert np.isclose(np.sum(np.abs(qc_two_qubits.register.get_state()) ** 2), 1.0)


def test_pauli_x(qc_two_qubits):
    # Apply Pauli-X to the second qubit
    qc_two_qubits.add_gate(paulix(), [1], "X")
    qc_two_qubits.execute()

    # Expected state: Flips the second qubit from |00> to |01>
    expected_state = np.zeros(2**qc_two_qubits.num_qubits, dtype=np.complex128)
    expected_state[1] = 1.0  # |01>

    assert np.allclose(qc_two_qubits.register.get_state(), expected_state)

    # Debug final state
    print(f"Final state vector: {qc_two_qubits.register.get_state()}")
    assert np.allclose(qc_two_qubits.register.get_state(), expected_state)


def test_clear_operations(qc_two_qubits):
    # Add some gates
    qc_two_qubits.add_gate(hadamard(), [0], "H")
    qc_two_qubits.add_gate(hadamard(), [1], "H")

    # Clear the operations
    qc_two_qubits.clear()
    qc_two_qubits.execute()

    # Expected state: Still |00> since operations were cleared
    expected_state = np.zeros(2**qc_two_qubits.num_qubits, dtype=np.complex128)
    expected_state[0] = 1.0  # |00>

    assert np.allclose(qc_two_qubits.register.get_state(), expected_state)


def test_dump_circuit(qc_two_qubits):
    # Add gates
    qc_two_qubits.add_gate(hadamard(), [0], "H")
    qc_two_qubits.add_gate(hadamard(), [1], "H")

    # Dump the circuit
    dumped_circuit = qc_two_qubits.dump_circuit()

    # Check the dumped operations
    assert len(dumped_circuit) == 2
    assert dumped_circuit[0][2] == "H"
    assert dumped_circuit[1][2] == "H"


def test_draw_circuit(qc_two_qubits, capsys):
    # Add gates
    qc_two_qubits.add_gate(hadamard(), [0], "H")
    qc_two_qubits.add_gate(cnot(), [0, 1], "CNOT")

    # Draw the circuit
    qc_two_qubits.draw_circuit(method="text")

    # Capture the printed output
    captured = capsys.readouterr()
    assert "H" in captured.out
    assert "●" in captured.out
    assert "X" in captured.out


if __name__ == "__main__":
    pytest.main()
