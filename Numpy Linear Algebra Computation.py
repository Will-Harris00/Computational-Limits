import numpy as np
import pandas as pd
import timeit as tm
import matplotlib.pyplot as plt


def main(nmax, iterations, repeats):
    global j
    time_dict = {}
    for n in range (1, nmax+1):
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

if __name__ == '__main__':
    j = 0
    main(20, 9999, 5)
    #times = time()
    #avg = cal_average(times[0], times[1], times[2], times[3])
    #curve(avg)
