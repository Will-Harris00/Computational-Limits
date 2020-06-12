import numpy as np


A = np.matrix([[1, 2, 3], [4, 5, 6], [0, 8, 9]])

def getMinor(A, i, j):
    return np.delete(np.delete(A, i, 0), j, 1)


def determinant(A):
    if A.size is 4:
        result = A[0, 0] * A[1, 1] - A[1, 0] * A[0, 1]
    else:
        result = 0
        for k in range(A.shape[1]):
            result += ((-1) ** k) * A[0, k] * determinant(getMinor(A, 0, k))

    return result

def inverse(A):
    C = np.zeros(A.shape)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            C[i, j] = ((-1) ** (i + j)) * determinant(getMinor(A, i, j))

    detA = 0
    for j in range(A.shape[1]):
        detA += C[0, j] * A[0, j]

    if abs(detA) == 0:
        raise Exception('This matrix is singular!')
    else:
        rmatrix = C.transpose() / detA
        return rmatrix
