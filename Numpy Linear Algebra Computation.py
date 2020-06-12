import numpy as np
import pandas as pd
import timeit as tm
import matplotlib.pyplot as plt


def main(nlist, iterations, repeats):
    global j
    time_dict = {}
    for n in nlist:
        j = n
        times_list = []
        for i in range (0, repeats):
            time = tm.timeit(matrix, number=iterations)
            print("\n " + str(n) + "x" +str(n) +" matrix run " + str(i + 1) +
                  " with " + str(iterations) +
                  " iterations completed in a time of " + str(time))
            times_list.append(time)

        sum = 0
        for t in times_list:
            sum = sum + t

        avg = sum / len(times_list)
        print("\nAverage time to complete one run of " +
              str(iterations) + " iterations for a random " + str(n) +
              "x" + str(n) + " matrix = " + str(avg) + "\n\n")

        time_dict.update({n: [n, avg]})
    print(time_dict)
    dataFrame(time_dict)


def matrix():
    global j
    nmatrix = np.random.rand(j, j)
    imatrix = np.linalg.inv(nmatrix)
    return imatrix


def dataFrame(time_dict):
    df = pd.DataFrame.from_dict(time_dict, orient='index', columns=['Size', 'Average Time'])
    print(df)
    df.plot(x='Size', y='Average Time', kind='line'
            , linestyle='solid', color='cyan', label='Numpy Linear Algorithm Method')
    print(time_dict)
    plt.xlabel('Size of n x n matrix')
    plt.ylabel('Average Time (seconds)')
    plt.show()

def setup():
    nvalues = []
    complete = True
    while len(nvalues) == 0:
        nval = input("Input the values of n that you wish to measure: ")
        try:
            nval = int(nval)
            nvalues.append(nval)
        except:
            print("\nPlease only enter integer numbers.")
            continue
    while len(nvalues) > 0:
        print(nvalues)
        nval = input("Continue to add values or enter 'start' begin measurements: ")
        try:
            nval = int(nval)
            nvalues.append(nval)
        except ValueError:
            if nval == 'start':
                break
    while complete:
        iterations = input("\nInput the number of iterations that you wish to measure: ")
        repeats = input("\nInput the number of repeats that you wish to measure: ")
        try:
            iterations = int(iterations)
            repeats = int(repeats)
            complete = False
        except ValueError:
            continue
    return nvalues, iterations, repeats


if __name__ == '__main__':
    j = 0
    setup = setup()
    main(setup[0], setup[1], setup[2])
