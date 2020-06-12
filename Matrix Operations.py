import numpy as np


def main():
    Q2017 = quantity(2017)
    Q2018 = quantity(2018)
    Q2019 = quantity(2019)
    print(Q2017)
    print("\n")
    print(Q2018)
    print("\n")
    print(Q2019)
    print("\n")

    C2017 = total_cost(2017)
    C2018 = total_cost(2018)
    C2019 = total_cost(2019)
    print(C2017)
    print("\n")
    print(C2018)
    print("\n")
    print(C2019)
    print("\n")

    I2017 = individual_price(Q2017, C2017)
    print(I2017)
    print("\n")
    I2018 = individual_price(Q2018, C2018)
    print(I2018)
    print("\n")
    I2019 = individual_price(Q2019, C2019)
    print(I2019)
    print("\n")

    stats17_18 = stats(I2017, I2018, 2017, 2018)
    print(stats17_18)
    print("\n")

    stats18_19 = stats(I2018, I2019, 2018, 2019)
    print(stats18_19)
    print("\n")

    stats17_19 = stats(I2017, I2019, 2017, 2019)
    print(stats17_19)
    print("\n")


def quantity(year):
    file = "Q" + str(year) + ".text"
    quantity_matrix = np.zeros(shape=(20,20),dtype=float)
    try:
        with open(file, 'r') as quantity_file:
            row = 0
            column = 0
            for line in quantity_file:
                try:
                    quantity_matrix[row][column] = line
                    column += 1
                    if column % 20 == 0:
                        column = 0
                        row += 1
                except IndexError:
                    break
    except FileNotFoundError:
        print("The file " + file + " does not exist.")
    return quantity_matrix

def total_cost(year):
    file = "C" + str(year) + ".text"
    cost_matrix = np.zeros(shape=(20,1),dtype=float)
    try:
        with open(file, 'r') as cost_file:
            row = 0
            for line in cost_file:
                try:
                    cost_matrix[row] = line
                    row += 1
                except IndexError:
                    break
    except FileNotFoundError:
        print("The file " + file + " does not exist.")
    return cost_matrix

def individual_price(qty_matrix, cost_matrix):
    indv_price = np.linalg.solve(qty_matrix, cost_matrix)
    price_matrix = np.matrix(indv_price)
    return price_matrix

def stats(previous, current, strt_year, end_year):
    stats_dict = {}
    prev_array = np.asarray(previous).reshape(-1)
    crnt_array = np.asarray(current).reshape(-1)
    print("Here is the data relating to growth period "+ str(strt_year) + "-"+ str(end_year) + "\n")
    for i in range(1,5):
        item_info = []
        prev = prev_array[i]
        actual = crnt_array[i]
        item = i + 1
        expected = prev * (1.03 ** (end_year-strt_year))
        real_diff = actual - expected
        page_diff = (real_diff / actual) * 100
        # Here we have a dictionary containing
        # the actual price of the item in the previous year
        # the actual price of the item in the current year
        # the expected value of the item in the current year
        # the difference between expected and actual price
        # start year and end year of the time period statistics
        # the item number is used as the key to access the dictionary values
        item_info.extend([prev, actual, expected, real_diff, page_diff, strt_year, end_year])
        stats_dict.update({item: item_info})
        print("Item "+ str(item) + ". Actual price = " + str(actual) +
              ", Expected price = " + str(expected) + ", Difference = "
              + str(real_diff) + ", Percentage difference = " + str(round(page_diff, 4)) +"%")
    return stats_dict

if __name__ == '__main__':
    main()
