import numpy as np
import pandas as pd
import timeit as tm
import matplotlib.pyplot as plt


def main(nlist, iterations, repeats):
    global j
    numpy_dict = {}
    cramer_dict = {}
    for n in nlist:
        j = n
        numpy_times = []
        cramer_times = []
        for i in range (0, repeats):
            cra_time = tm.timeit(cramer, number=iterations)
            num_time = tm.timeit(numpy, number=iterations)
            print("\nNumpy Linear Algorithm Method - " + str(n) + "x" +str(n) +" matrix run " + str(i + 1) +
                  " with " + str(iterations) +
                  " iterations completed in a time of " + str(num_time))
            print("\nCramer's Recursive Method - " + str(n) + "x" +str(n) +" matrix run " + str(i + 1) +
                  " with " + str(iterations) +
                  " iterations completed in a time of " + str(cra_time))
            numpy_times.append(num_time)
            cramer_times.append(cra_time)


        numpy_sum = 0
        for t in numpy_times:
            numpy_sum = numpy_sum + t

        cramer_sum = 0
        for u in cramer_times:
            cramer_sum = cramer_sum + u

        num_avg = numpy_sum / len(numpy_times)
        cra_avg = cramer_sum / len(cramer_times)
        print("\n\nNumpy Linear Algorithm Method - Average time to complete one run of " +
              str(iterations) + " iterations for a random " + str(n) +
              "x" + str(n) + " matrix = " + str(num_avg))
        print("\nCramer's Recursive Method - Average time to complete one run of " +
              str(iterations) + " iterations for a random " + str(n) +
              "x" + str(n) + " matrix = " + str(cra_avg) + "\n\n")
        numpy_dict.update({n: [n, num_avg]})
        cramer_dict.update({n: [n, cra_avg]})
        print("not quite finished - please wait")
    print(numpy_dict)
    print(cramer_dict)
    dataFrame(numpy_dict, cramer_dict, nlist[0], nlist[-1])


def numpy():
    global j
    nmatrix = np.random.rand(j, j)
    imatrix = np.linalg.inv(nmatrix)
    return imatrix

def cramer():
    global j
    rmatrix = np.random.rand(j, j)
    cmatrix = inverse(rmatrix)
    return cmatrix


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
        imatrix = C.transpose() / detA
        return imatrix


def dataFrame(numpy_dict, cramer_dict, nmin, nmax):
    numpy_df = pd.DataFrame.from_dict(numpy_dict, orient='index', columns=['Size', 'Average Time'])
    print(numpy_df)
    cramer_df = pd.DataFrame.from_dict(cramer_dict, orient='index', columns=['Size', 'Average Time'])
    print(cramer_df)
    print("finished")
    plt.plot('Size', 'Average Time', data=numpy_df, marker='D', markerfacecolor='skyblue', markersize=5, color='skyblue',
             linewidth=2, label='Numpy Linear Algorithm Method')
    plt.plot('Size', 'Average Time', data=cramer_df, marker='o', markerfacecolor='pink', markersize=5, color='pink',
             linewidth=2, label="Cramer's Recursive Method")
    plt.legend()
    plt.xlabel("Size 'n' of square matrix")
    plt.ylabel("Average Time (seconds)")
    plt.xticks(np.arange(nmin, nmax+1, step=1.0))
    plt.show()

def setup():
    nvalues = []
    not_complete = True
    while len(nvalues) == 0:
        nval = input("Input the values of n that you wish to measure: ")
        try:
            nval = int(nval)
            nvalues.append(nval)
        except:
            print("\nPlease only enter integer numbers.")
            continue
    while len(nvalues) > 0:
        nvalues.sort()
        print(nvalues)
        nval = input("Continue to add values or enter 'start' begin measurements: ")
        try:
            nval = int(nval)
            try:
                nvalues.index(nval)
                continue
            except ValueError:
                nvalues.append(nval)
        except ValueError:
            if nval == 'start':
                break
    while not_complete:
        iterations = input("\nInput the number of iterations that you wish to measure: ")
        repeats = input("\nInput the number of repeats that you wish to measure: ")
        try:
            iterations = int(iterations)
            repeats = int(repeats)
            not_complete = False
        except ValueError:
            continue
    return nvalues, iterations, repeats


if __name__ == '__main__':
    j = 0
    setup = setup()
    main(setup[0], setup[1], setup[2])
