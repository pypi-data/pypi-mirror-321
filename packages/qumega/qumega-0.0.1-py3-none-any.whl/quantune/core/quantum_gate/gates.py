import numpy as np
from numpy.typing import NDArray


def identity() -> NDArray:
    """Identity gate as a 2x2 matrix.

    ```
    I = [[1, 0],
         [0, 1]]
    ```
    Returns:
        NDArray: Matrix representation of the identity gate.
    """
    return np.array([[1, 0], [0, 1]], dtype=np.complex128)


def paulix() -> NDArray:
    """Pauli-X gate as a 2x2 matrix.

    ```
    X = [[0, 1],
         [1, 0]]
    ```
    Returns:
        NDArray: Matrix representation of the pauli-x gate.
    """
    return np.array([[0, 1], [1, 0]], dtype=np.complex128)


def pauliy() -> NDArray:
    """Pauli-Y gate as a 2x2 matrix.

    ```
    Y = [[0, -i],
         [i,  0]]
    ```
    Returns:
        NDArray: Matrix representation of the pauli-y gate.
    """
    return np.array([[0, -1j], [1j, 0]], dtype=np.complex128)


def pauliz() -> NDArray:
    """Pauli-Z gate as a 2x2 matrix.

    ```
    Z = [1,  0]
        [0, -1]
    ```
    Returns:
        NDArray: Matrix representation of the pauli-z gate.
    """
    return np.array([[1, 0], [0, -1]], dtype=np.complex128)


def hadamard() -> NDArray:
    """Hadamard gate as a 2x2 matrix.

    ```
    Hadamard = (1/sqrt(2))  *  [[1,  1],
                                [1, -1]]
    ```
    Returns:
        NDArray: Matrix representation of the hadamard gate.
    """
    return (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=np.complex128)


def phase(theta: float = np.pi / 2) -> NDArray[np.complex128]:
    """Phase gate as a 2x2 matrix.

    ```
    Phase = [[1, 0],
             [0, e^(i * θ)]]
    ```
    Args:
        theta (float, optional): Angle of vector. Defaults to np.pi/2.

    Returns:
        NDArray: Matrix representation of the phase gate.
    """
    return np.array([[1, 0], [0, np.exp(1j * theta)]], dtype=np.complex128)


def s() -> NDArray:
    """S gate as a 2x2 matrix.

    ```
    S = [[1, 0],
         [0, i]]
    ```
    Returns:
        NDArray: Matrix representation of the S gate.
    """
    return np.array([[1, 0], [0, 1j]], dtype=np.complex128)


def sdg() -> NDArray:
    """SDG gate as a 2x2 matrix.

    ```
    SDG = [[1, 0],
           [0, -i]]
    ```
    Returns:
        NDArray: Matrix representation of the SDG gate.
    """
    return np.array([[1, 0], [0, -1j]], dtype=np.complex128)


def t() -> NDArray:
    """T gate as a 2x2 matrix.

    ```
    T = [[1, 0],
         [0, e^((i * pi) / 4]]
    ```
    Returns:
        NDArray: Matrix representation of the T gate.
    """
    return np.array([[1, 0], [0, np.exp((1j * np.pi) / 4)]], dtype=np.complex128)


def tdg() -> NDArray:
    """TDG gate as a 2x2 matrix.

    ```
    TDG = [[1, 0],
           [0, e^((-i * pi) / 4]]
    ```
    Returns:
        NDArray: Matrix representation of the TDG gate.
    """
    return np.array([[1, 0], [0, np.exp((-1j * np.pi) / 4)]], dtype=np.complex128)


def rz(theta: float = np.pi / 2) -> NDArray:
    """RZ gate as a 2x2 matrix.

    ```
    RZ =    [[e^(-i * (θ / 2)), 0],
             [0,  e^(i * (θ / 2))]]
    ```
    Args:
        theta (float, optional): Angle of vector. Defaults to np.pi/2.

    Returns:
        NDArray: Matrix representation of the RZ gate.
    """
    return np.array(
        [[np.exp(-1j * (theta / 2)), 0], [0, np.exp(1j * (theta / 2))]],
        dtype=np.complex128,
    )


def rx(theta: float = np.pi / 2) -> NDArray:
    """RX gate as a 2x2 matrix.

    ```
    RX =   [[cos(θ / 2), -i * sin(θ / 2)],
            [-i * sin(θ / 2),  cos(θ / 2)]]
    ```
    Args:
        theta (float, optional): Angle of vector. Defaults to np.pi/2.

    Returns:
        NDArray: Matrix representation of the RX gate.
    """
    return np.array(
        [
            [np.cos(theta / 2), -1j * np.sin(theta / 2)],
            [-1j * np.sin(theta / 2), np.cos(theta / 2)],
        ],
        dtype=np.complex128,
    )


def ry(theta: float = np.pi / 2) -> NDArray:
    """RY gate as a 2x2 matrix.


    ```
    RY =    [[cos(θ / 2), -1 * sin(θ / 2)],
             [sin(θ / 2),  cos(θ / 2)]]
    ```
    Args:
        theta (float, optional): Angle of vector. Defaults to np.pi/2.

    Returns:
        NDArray: Matrix representation of the RY gate.
    """
    return np.array(
        [
            [np.cos(theta / 2), -1 * np.sin(theta / 2)],
            [np.sin(theta / 2), np.cos(theta / 2)],
        ],
        dtype=np.complex128,
    )


def sx() -> NDArray:
    """SX gate as a 2x2 matrix.

    ```
    SX =    [[1 + i, 1 - i],
             [1 - i, 1 + i]]  * (1 / 2)
    ```
    Returns:
        NDArray: Matrix representation of the SX gate.
    """
    return np.array([[1 + 1j, 1 - 1j], [1 - 1j, 1 + 1j]], dtype=np.complex128) / 2


def sxdg() -> NDArray:
    """SXDG gate as a 2x2 matrix.

    ```
    SXDG =  [[1 - i, 1 + i],
             [1 + i, 1 - i]] * (1 / 2)
    ```
    Returns:
        NDArray: Matrix representation of the SXDG gate.
    """
    return (1 / 2) * np.array([[1 - 1j, 1 + 1j], [1 + 1j, 1 - 1j]], dtype=np.complex128)


def u(
    theta: float = np.pi / 2, phi: float = np.pi / 2, lmbda: float = np.pi / 2
) -> NDArray:
    """U gate as a 2x2 matrix.

    ```
    u = [[cos(θ / 2), -1 * e^(i * λ) * sin(θ / 2)],
         [e^(i * φ) * sin(θ / 2), e^(i * (λ + φ)) * cos(θ / 2)]]
    ```
    Args:
        theta (float, optional): Rotation angle (0 to π) determining the degree of rotation. Defaults to np.pi/2.
        phi (float, optional): Phase shift affecting the qubit's state on the Bloch sphere. Defaults to np.pi/2.
        lmbda (float, optional): Additional phase shift influencing interference patterns. Defaults to np.pi/2.

    Returns:
        NDArray: Matrix representation of the U gate.
    """
    return np.array(
        [
            [np.cos(theta / 2), -1 * np.exp(1j * lmbda) * np.sin(theta / 2)],
            [
                np.exp(1j * phi) * np.sin(theta / 2),
                np.exp(1j * (lmbda + phi)) * np.cos(theta / 2),
            ],
        ],
        dtype=np.complex128,
    )


def r1(theta: float = np.pi / 2) -> NDArray:
    """
    R1 gate as a 2x2 matrix.

    ```
    R1 =    [[1, 0],
             [0, e^(i * θ)]]
    ```
    Args:
        theta (float, optional): Rotation angle. Defaults to np.pi/2.

    Returns:
        NDArray: Matrix representation of the R1 gate.
    """
    return np.array([[1, 0], [0, np.exp(1j * theta)]], dtype=np.complex128)


def cnot() -> NDArray:
    """CNOT gate as a 4x4 matrix.

    ```
    CNOT = [[1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]]
    ```
    Returns:
        NDArray: Matrix representation of the CNOT gate.
    """
    return np.array(
        [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], dtype=np.complex128
    )


def swap() -> NDArray:
    """Swap gate as a 4x4 matrix.

    ```
    Swap = [[1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]]
    ```
    Returns:
        NDArray: Matrix representation of the swap gate.
    """
    return np.array(
        [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], dtype=np.complex128
    )


def toffoli() -> NDArray:
    """Toffoli gate as a 8x8 matrix.

    ```
    Toffoli =  [[1, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 1, 0]]
    ```
    Returns:
        NDArray: Matrix representation of the toffoli gate.
    """
    return np.array(
        [
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 0],
        ],
        dtype=np.complex128,
    )


def rxx(theta: float = np.pi / 2) -> NDArray:
    """RXX gate as a 4x4 matrix.

    ```
    RXX(θ) =    [[cos(θ / 2), 0, 0, -i * sin(θ / 2)],
                 [0, cos(θ / 2), -i * sin(θ / 2), 0],
                 [0, -i * sin(θ / 2), cos(θ / 2), 0],
                 [-i * sin(θ / 2), 0, 0, cos(θ / 2)]]
    ```
    Args:
        theta (float, optional): Rotation angle. Defaults to np.pi/2.

    Returns:
        NDArray: Matrix representation of the RXX gate.
    """
    return np.array(
        [
            [np.cos(theta / 2), 0, 0, -1j * np.sin(theta / 2)],
            [0, np.cos(theta / 2), -1j * np.sin(theta / 2), 0],
            [0, -1j * np.sin(theta / 2), np.cos(theta / 2), 0],
            [-1j * np.sin(theta / 2), 0, 0, np.cos(theta / 2)],
        ],
        dtype=np.complex128,
    )


def rzz(theta: float = np.pi / 2) -> NDArray:
    """RZZ gate as a 4x4 matrix.

    ```
    RZZ = [[e^(-i * (θ / 2)), 0, 0, 0],
           [0,  e^(i * (θ / 2)), 0, 0],
           [0, 0,  e^(i * (θ / 2)), 0],
           [0, 0, 0, e^(-i * (θ / 2))]]
    ```
    Args:
        theta (float, optional): Rotation angle. Defaults to np.pi/2.

    Returns:
        NDArray: Matrix representation of the RZZ gate.
    """
    return np.array(
        [
            [np.exp(-1j * (theta / 2)), 0, 0, 0],
            [0, np.exp(1j * (theta / 2)), 0, 0],
            [0, 0, np.exp(1j * (theta / 2)), 0],
            [0, 0, 0, np.exp(-1j * (theta / 2))],
        ],
        dtype=np.complex128,
    )


def cr(theta: float = np.pi / 2) -> NDArray:
    """CR gate as a 4x4 matrix.

    ```
    CR = [[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, e^(θ * i)]]
    ```
    Args:
        theta (float, optional): Rotation angle. Defaults to np.pi/2.

    Returns:
        NDArray: Matrix representation of the CR gate.
    """
    return np.array(
        [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, np.exp(theta * 1j)]],
        dtype=np.complex128,
    )


def cz() -> NDArray:
    """CZ gate as a 4x4 matrix.

    ```
    CZ = [[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, -1]]
    ```
    Returns:
        NDArray: Matrix representation of the CZ gate.
    """
    return np.array(
        [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]], dtype=np.complex128
    )
