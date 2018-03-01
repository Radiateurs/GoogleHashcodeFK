import numpy as np


def read_inut(filename):
    def str_to_bool_array(s, true='T'):
        return [bool(c == true) for c in s]

    with open(filename, 'r') as file:
        header = file.readline()
        data = file.read()

    ingredients = header.split()[2]
    max_area = header.split()[3]
    pizza = np.array([str_to_bool_array(s) for s in data.split()])
    return int(ingredients), int(max_area), pizza


def read_inputs(filename):
	with open(filename, 'r') as file:
        header = file.readline()
        rows = header.split()[0]
        columns = header.split()[1]
        vehicles = header.split()[2]
        rides = header.split()[3]
        bonus = header.split()[4]
        steps = header.split()[5]
        mat = np.zeros((rides, 3, 2))
        for i in range(rides):
        	line = file.readline()
        	mat[i, 0, :] = line.split()[0:2]
        	mat[i, 1, :] = line.split()[2:4]
        	mat[i, 2, :] = line.split()[4:6]
    return mat, rows, columns, vehicles, rides, bonus, steps
