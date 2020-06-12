import numpy as np
import pandas as pd
import timeit as t
import matplotlib.pyplot as plt


def matrix5():
    nfive_matrix = np.random.rand(5, 5)
    ifive_matrix = np.linalg.inv(nfive_matrix)
    return ifive_matrix

def matrix10():
    nten_matrix = np.random.rand(10, 10)
    iten_matrix = np.linalg.inv(nten_matrix)
    return iten_matrix

def matrix20():
    ntwenty_matrix = np.random.rand(20, 20)
    itwenty_matrix = np.linalg.inv(ntwenty_matrix)
    return itwenty_matrix

def matrix50():
    nfifty_matrix = np.random.rand(50, 50)
    ififty_matrix = np.linalg.inv(nfifty_matrix)
    return ififty_matrix

def time():
    iterations = 9999
    timing5 = []
    timing10 = []
    timing20 = []
    timing50 = []
    for i in range (5):
        time5 = t.timeit(matrix5, number=iterations)
        print("\n 5x5 matrix run " + str(i+1) + " with " + str(iterations) +
              " iterations completed in a time of "+ str(time5))
        timing5.append(time5)

        time10 = t.timeit(matrix10, number=iterations)
        print("\n 10x10 matrix run " + str(i+1) + " with " + str(iterations) +
              " iterations completed in a time of "+ str(time10))
        timing10.append(time10)

        time20 = t.timeit(matrix20, number=iterations)
        print("\n 20x20 matrix run " + str(i+1) + " with " + str(iterations) +
              " iterations completed in a time of "+ str(time20))
        timing20.append(time20)

        time50 = t.timeit(matrix50, number=iterations)
        print("\n 50x50 matrix run " + str(i+1) + " with " + str(iterations) +
              " iterations completed in a time of "+ str(time50))
        timing50.append(time50)
        print("\n")
    print(str(timing5) + "\n" + str(timing10) + "\n" + str(timing20) + "\n" + str(timing50) + "\n")
    return timing5, timing10, timing20, timing50

def cal_average(timing5, timing10, timing20, timing50):
    sum_num = 0
    for t in timing5:
        sum_num = sum_num + t

    avg5 = sum_num / len(timing5)
    print("Average time to complete one run of 9999 iterations "
          "for a random 5x5 matrix " +str(avg5))

    sum_num = 0
    for t in timing10:
        sum_num = sum_num + t

    avg10 = sum_num / len(timing10)
    print("Average time to complete one run of 9999 iterations "
          "for a random 10x10 matrix " +str(avg10))

    sum_num = 0
    for t in timing20:
        sum_num = sum_num + t

    avg20 = sum_num / len(timing20)
    print("Average time to complete one run of 9999 iterations "
          "for a random 20x20 matrix " +str(avg20))

    sum_num = 0
    for t in timing50:
        sum_num = sum_num + t

    avg50 = sum_num / len(timing50)
    print("Average time to complete one run of 9999 iterations "
          "for a random 50x50 matrix " +str(avg50))

    return avg5, avg10, avg20, avg50


def curve(avg):
    time_dict = {}
    time_dict.update({5 : [5, avg[0]]})
    time_dict.update({10 : [10, avg[1]]})
    time_dict.update({20 : [20, avg[2]]})
    time_dict.update({50 : [50, avg[3]]})
    df = pd.DataFrame.from_dict(time_dict, orient='index', columns=['Size', 'Average Time'])
    print(df)
    df.plot(x='Size', y='Average Time', kind='line'
            , linestyle='solid', color='cyan', label='Numpy Linear Algorithm Method')
    print(time_dict)
    plt.xlabel('Size of n x n matrix')
    plt.ylabel('Average Time (seconds)')
    plt.show()

if __name__ == '__main__':
    times = time()
    avg = cal_average(times[0], times[1], times[2], times[3])
    curve(avg)
