import numpy as np

def distances_list(vehicles, ride):
    distance = np.zeros(vehicles.shape[0])
    for i, vehicle in enumeration(vehicles):
        distance[i] = (max(vehicle[0], ride[0]) - min(vehicle[0], ride[0])) + (max(vehicle[1], ride[1]) - min(vehicle[1], ride[1]))
    return distance

def sort_rides(rides):
    def sorter(ride):
        return ride[2][0]
    return np.array(sorted([r for r in rides], key=sorter))