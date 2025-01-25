import numpy as np
from scipy.optimize import minimize
from quantum_gate.gates import *

# -------------------------- Hamiltonian Class -------------------------- #
class Hamiltonian:
    def __init__(self, pauli_sum, num_qubits):
        """
        Initialize the Hamiltonian from a list of Pauli terms.
        Args:
            pauli_sum (list): List of (Pauli string, coefficient) tuples.
            num_qubits (int): Number of qubits in the system.
        """
        self.pauli_sum = pauli_sum
        self.num_qubits = num_qubits

    def evaluate(self, state):
        """
        Compute the expectation value of the Hamiltonian.
        """
        expectation_value = 0
        for pauli_string, coeff in self.pauli_sum:
            term_expectation = self._evaluate_pauli_term(state, pauli_string)
            expectation_value += coeff * term_expectation
        return expectation_value

    def _evaluate_pauli_term(self, state, pauli_string):
        """
        Evaluate the expectation value for a single Pauli term.
        """
        rotated_state = self._apply_basis_rotation(state, pauli_string)

        if all(p in ['I', 'Z'] for p in pauli_string):
            probabilities = np.abs(rotated_state) ** 2
            return self._compute_z_expectation(probabilities, pauli_string)

        pauli_map = {
            'I': identity(),
            'X': paulix(),
            'Y': pauliy(),
            'Z': pauliz()
        }

        operator = 1
        for p in pauli_string:
            operator = np.kron(operator, pauli_map[p])

        return np.real(np.conj(rotated_state.T) @ operator @ rotated_state)[0, 0]

    def _apply_basis_rotation(self, state, pauli_string):
        """
        Rotate the quantum state into the measurement basis for the given Pauli string
        by applying appropriate single-qubit rotations.
        """
        dim = len(state)
        num_qubits = int(np.log2(dim))
        rotated_state = state

        for i, p in enumerate(pauli_string):
            if p == 'I':
                continue
            elif p == 'X':
                rotation = hadamard()  
            elif p == 'Y':
                rotation = np.array([[1, -1j], [1j, -1]]) / np.sqrt(2)  # S†H
            else:
                continue

            # Construct the full rotation matrix for the qubit
            left_identity = np.eye(2**i, dtype=complex)
            right_identity = np.eye(2**(num_qubits - i - 1), dtype=complex)
            full_rotation = np.kron(np.kron(left_identity, rotation), right_identity)

            rotated_state = full_rotation @ rotated_state

        return rotated_state

    def _compute_z_expectation(self, probabilities, pauli_string):
        """
        Compute the expectation value from probabilities for Z-only Pauli strings.
        """
        expectation = 0
        dim = len(probabilities)
        num_qubits = int(np.log2(dim))

        for i, p in enumerate(pauli_string):
            if p == 'Z':
                indices_with_1 = [j for j in range(dim) if (j >> (num_qubits - i - 1)) & 1]
                prob_1 = np.sum(probabilities[indices_with_1])
                prob_0 = np.sum(probabilities) - prob_1
                expectation += prob_0 - prob_1

        return expectation

# -------------------------- Ansatz Class -------------------------- #
def embed_cnot(num_qubits, control, target):
    """Embed a 4x4 CNOT gate into a 2^n x 2^n matrix for n-qubits."""
    dim = 2**num_qubits
    cnot_matrix = np.eye(dim, dtype=complex)
    for i in range(dim):
        control_bit = (i >> (num_qubits - control - 1)) & 1
        if control_bit == 1:  
            flipped_index = i ^ (1 << (num_qubits - target - 1))
            cnot_matrix[flipped_index, i] = 1
            cnot_matrix[i, i] = 0
    return cnot_matrix

class Ansatz:
    def __init__(self, num_qubits, num_layers=1):
        """
        Improved Ansatz with RY, RZ, and entangling CNOT gates.
        Args:
            num_qubits (int): Number of qubits.
            num_layers (int): Number of layers in the circuit.
        """
        self.num_qubits = num_qubits
        self.num_layers = num_layers

    def create_ansatz(self, params):
        """
        Generate the parameterized quantum circuit.
        Args:
            params (list): Rotation angles for RY and RZ gates.
        Returns:
            np.array: State vector after applying the ansatz.
        """
        dim = 2**self.num_qubits
        state = np.zeros(dim, dtype=complex)
        state[0] = 1.0
        state = state.reshape(-1, 1)

        param_idx = 0
        for layer in range(self.num_layers):
            # Apply parameterized RY and RZ rotations to each qubit
            for qubit in range(self.num_qubits):
                
                theta_ry = params[param_idx]
                theta_rz = params[param_idx + 1]
                param_idx += 2

                # Apply RY rotation
                left_dims = 2**qubit
                right_dims = 2**(self.num_qubits - qubit - 1)
                rotation = ry(theta_ry)
                operation = np.kron(np.eye(left_dims), np.kron(rotation, np.eye(right_dims)))
                state = operation @ state

                # Apply RZ rotation
                rotation = rz(theta_rz)
                operation = np.kron(np.eye(left_dims), np.kron(rotation, np.eye(right_dims)))
                state = operation @ state

            if layer < self.num_layers - 1:
                # Even-odd pattern
                for control in range(0, self.num_qubits - 1, 2):
                    target = control + 1
                    cnot_matrix = embed_cnot(self.num_qubits, control, target)
                    state = cnot_matrix @ state

                # Odd-even pattern
                for control in range(1, self.num_qubits - 1, 2):
                    target = control + 1
                    cnot_matrix = embed_cnot(self.num_qubits, control, target)
                    state = cnot_matrix @ state

        return state

# -------------------------- Optimizer Class -------------------------- #
class Optimizer:
    def __init__(self, method="GD", learning_rate=0.1, momentum=0.9, beta1=0.9, beta2=0.999, epsilon=1e-8):
        """
        Initialize the optimizer.
        Args:
            method (str): Optimization method ('GD', 'NAG', 'Adam', 'COBYLA').
            learning_rate (float): Learning rate for optimization.
            momentum (float): Momentum coefficient (used in NAG).
            beta1 (float): Exponential decay rate for first moment estimates (Adam).
            beta2 (float): Exponential decay rate for second moment estimates (Adam).
            epsilon (float): Small value to prevent division by zero (Adam).
        """
        self.method = method
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.velocity = None  
        self.t=0
        self.m = None
        self.v = None

    def optimize(self, func, initial_params, max_iter=100, tol=1e-6):
        """
        Optimize the given function.
        """
        params = np.array(initial_params, dtype=float)
        history = []

        if self.method in ["GD", "NAG"]:
            if self.velocity is None:
                self.velocity = np.zeros_like(params)

        for _ in range(max_iter):
            if self.method in ["GD", "NAG", "Adam"]:
                grad = self._finite_difference_gradient(func, params)

            if self.method == "GD":
                # Gradient Descent
                params -= self.learning_rate * grad

            elif self.method == "NAG":
                # Nesterov Accelerated Gradient
                lookahead_params = params - self.momentum * self.velocity
                grad = self._finite_difference_gradient(func, lookahead_params)
                self.velocity = self.momentum * self.velocity + self.learning_rate * grad
                params -= self.velocity

            elif self.method == "Adam":
                # Adam Optimizer
                self.t += 1
                if self.m is None or self.v is None:
                    self.m = np.zeros_like(params)
                    self.v = np.zeros_like(params)

                self.m = self.beta1 * self.m + (1 - self.beta1) * grad
                self.v = self.beta2 * self.v + (1 - self.beta2) * (grad**2)

                m_hat = self.m / (1 - self.beta1**self.t)
                v_hat = self.v / (1 - self.beta2**self.t)

                params -= self.learning_rate * m_hat / (np.sqrt(v_hat) + self.epsilon)

            elif self.method == "COBYLA":
                # COBYLA Optimizer
                result = minimize(func, initial_params, method="COBYLA", options={"maxiter": max_iter, "tol": tol})
                params = result.x
                history.append(result.fun)
                break

            energy = func(params)
            history.append(energy)

            if len(history) > 1 and abs(history[-1] - history[-2]) < tol:
                break

        return {"optimal_parameters": params, "energy_history": history, "converged": True}

    def _finite_difference_gradient(self, func, params, epsilon=1e-6):
        """
        Compute gradients using the finite difference method.
        """
        grad = np.zeros_like(params)
        for i in range(len(params)):
            params[i] += epsilon
            f_plus = func(params)
            params[i] -= 2 * epsilon
            f_minus = func(params)
            params[i] += epsilon
            grad[i] = (f_plus - f_minus) / (2 * epsilon)
        return grad


# -------------------------- VQE Class -------------------------- #
class VQE:
    def __init__(self, hamiltonian, ansatz, optimizer):
        """
        Initialize the VQE algorithm.
        Args:
            hamiltonian (Hamiltonian): The Hamiltonian object.
            ansatz (callable): Ansatz function to generate the quantum state.
            optimizer (Optimizer): Optimizer object.
        """
        self.hamiltonian = hamiltonian
        self.ansatz = ansatz
        self.optimizer = optimizer
        self.energy_history = []

    def run(self, initial_params, max_iter=100, tol=1e-6):
        """Run the VQE optimization."""
        def cost_function(params):
            state = self.ansatz.create_ansatz(params)
            return self.hamiltonian.evaluate(state)  

        result = self.optimizer.optimize(cost_function, initial_params, max_iter, tol)
        optimal_params = result['optimal_parameters']
        ground_state_energy = result['energy_history'][-1]  # Get the final energy from history

        self.ground_state_energy = ground_state_energy
        self.optimal_params = optimal_params
        return ground_state_energy, optimal_params

    def get_results(self):
      # Print results
      print(f"Final Energy: {self.ground_state_energy:.6f}")
      print("Optimal Parameters:", self.optimal_params)

# -------------------------- Example Usage -------------------------- #
if __name__ == "__main__":
    h2_hamiltonian = Hamiltonian([
        ("II", -1.052373245772859),
        ("ZI", 0.39793742484318045),
        ("IZ", 0.39793742484318045),
        ("ZZ", -0.01128010425623538),
        ("XX", 0.18093119978423156)
    ],2)

    num_qubits = 2
    num_layers = 2
    ansatz = Ansatz(2,2)  
    optimizer = Optimizer(method='Adam', learning_rate=0.05)  

    # Initialize VQE
    vqe = VQE(hamiltonian=h2_hamiltonian, ansatz=ansatz, optimizer=optimizer)

    # Generate initial parameters
    initial_params = np.random.uniform(size=num_qubits * num_layers * 2)

    # Run VQE
    result = vqe.run(initial_params=initial_params, max_iter=100, tol=1e-6)

    vqe.get_results()
