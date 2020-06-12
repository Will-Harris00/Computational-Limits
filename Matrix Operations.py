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

    growth17_18 = growth(I2017, I2018, 2017, 2018)
    print(growth17_18)
    print("\n")
    growth18_19 = growth(I2018, I2019, 2018, 2019)
    print(growth18_19)
    print("\n")
    growth17_19 = growth(I2017, I2019, 2017, 2019)
    print(growth17_19)
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

def growth(previous, current, strt_year, end_year):
    growth = []
    prev_array = np.asarray(previous).reshape(-1)
    crnt_array = np.asarray(current).reshape(-1)
    for i in range(1,5):
        prev = prev_array[i]
        crnt = crnt_array[i]
        difference = crnt - prev
        growth.append((difference / prev) * 100)
        print("Percentage growth of item "+ str(i+1) +" starting at £" +
              str(prev) + " and ending at £" + str(crnt) + " = " +
              str(((difference / prev) * 100))
              + "% for the year " + str(strt_year) + " to " + str(end_year))
    return growth


if __name__ == '__main__':
    main()
