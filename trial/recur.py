

import numpy as np


def divide_and_conqueer(mat, L, H):
    """
    heyyy
    """
    return 0


def rec(mat, L, h):
    lct = 0
    lcm = 0
    h = 0
    mask = np.zeros(mat.shape)
    b = np.array([0, 0])
    e = np.array([0, 0])
    e, lcm, lct = add(mat, e, np.array([1, 0]), h, lcm, lct)


def add(mat, e, a, h, lcm, lct):
    e += a
    if e.sum() < h:
        v = mat[e - a, e]
        for i in matc:
            print i
            if i:
                lct += 1
            else:
                lcm += 1
        if e[0] + 1 <= mat.shape[0]
            e, lcm, lct = add(mat, e, np.array([0, 1]), h, lcm, lct)
            if e and lcm > h and lct > h:
                return e, lcm, lct

        e, lcm, lct = add(mat, e, np.array([0, 1]), h, lcm, lct)
        if e and lcm > h and lct > h:
            return e, lcm, lct

        return False, lcm, lct
