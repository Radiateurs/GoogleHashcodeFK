import numpy as np

def read_input(filename):
    def str_to_bool_array(s, true='T'):
        return [bool(c == true) for c in s]

    with open(filename, 'r') as file:
        header = file.readline()
        data = file.read()

    ingredients = header.split()[2]
    max_area = header.split()[3]
    pizza = np.array([str_to_bool_array(s) for s in data.split()])
    return int(ingredients), int(max_area), pizza
