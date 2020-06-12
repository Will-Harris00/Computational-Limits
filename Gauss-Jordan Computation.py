import numpy as np


# convenience function for getting the minor Mij
def getMinor(A, i, j):
    return np.delete(np.delete(A, i, 0), j, 1)


# recursive function for calculating the determinant
def determinant(A):
    if A.size is 4:
        result = A[0, 0] * A[1, 1] - A[1, 0] * A[0, 1]
    else:
        # calculate minors for all columns
        result = 0
        for k in range(A.shape[1]):
            result += ((-1) ** k) * A[0, k] * determinant(getMinor(A, 0, k))

    return result


# Inverse
# Build on the code you wrote for part one to provide the Cramer's rule solution to calculate the inverse of a matrix (as discussed in the lecture). Again compare your approach to numpy's results on some matrices.
def inverse(A):
    # calculate matrix of cofactors
    C = np.zeros(A.shape)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            C[i, j] = ((-1) ** (i + j)) * determinant(getMinor(A, i, j))

    # calculate the determinant
    detA = 0
    for j in range(A.shape[1]):
        detA += C[0, j] * A[0, j]

    # check whether the determinant is nonzero
    if abs(detA) == 0:
        raise Exception('This matrix is singular!')
    else:
        # calculate the inverse
        return C.transpose() / detA

#Create the 3 x 3 matrix equation problem
A = np.matrix([[3,4,9],[6,7,9],[9,10,11]])
b = np.matrix([13,7.0,3.0]).T
# Check that it works
x = inverse(A)*b
print(x)


C = np.matrix([[1, 1, 2], [0, 2, 2], [1, 0, 3]])
d = np.matrix([0, 2, 1]).T
y = inverse(C)*d
print(y)
