import numpy as np


A = np.matrix([[1, 2, 3], [4, 5, 6], [0, 8, 9]])
print(A)

# convenience function for getting the minor Mij
def getMinor(A, i, j):
    return np.delete(np.delete(A, i, 0), j, 1)


# demonstration
for i in range(3):
    print('---')
    for j in range(3):
        print(getMinor(A, i, j))
print('----')


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


print(determinant(A))
print(np.linalg.det(A))


# Exercise 2: Inverse
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


print(A)
print(inverse(A))
print(np.linalg.inv(A))
