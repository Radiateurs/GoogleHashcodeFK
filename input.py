import numpy as np


def read_inputs(filename):

    with open(filename, 'r') as file:
        header = file.readline()
        rows = int(header.split()[0])
        columns = int(header.split()[1])
        vehicles = int(header.split()[2])
        rides = int(header.split()[3])
        bonus = int(header.split()[4])
        steps = int(header.split()[5])
        mat = np.zeros((rides, 4, 2))
        for i in range(rides):
            line = file.readline()
            mat[i, 0, :] = (int(line.split()[0]), int(line.split()[1]))
            mat[i, 1, :] = (int(line.split()[2]), int(line.split()[3]))
            mat[i, 2, :] = (int(line.split()[4]), int(line.split()[5]))
            mat[i, 3] = i
    return mat, rows, columns, vehicles, rides, bonus, steps
