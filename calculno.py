import numpy as np
import itertools
from functools import partial
import decimal

def grad_descent(func):

    def num_deriv(x):
        dx = 10 ** -10
        return (func(x + dx) - func(x)) / dx

    def find_local_min(x):
        delt = 10 ** -10
        i = 0
        while (abs(num_deriv(x)) >= delt and i < 10 ** 4):
            res_sum = 0
            nd = num_deriv(x)
            if x - 0.1 * nd > 0 and x - 0.1 * nd < 10000:
                x = x - 0.1 * nd
            else:
                break

            i = i + 1
        return (func(x), x)

    arr_lm = [(i * 100) for i in range(0, 100)]
    m = min(list(map(find_local_min, arr_lm)))
    return tuple(m)

def square_eror(arr, a):
    return sum([(y - x * a) ** 2 for x, y in arr]) / len(arr)

def comb(arr):
    arr1 = list()
    for i in range(3, len(arr) + 1):
        for i in itertools.combinations(arr, i):
            arr1.append(i)
    return arr1

table = [(0.000834274292,	0.048526),
         (0.000834274292,	0.048477),
         (0.001668548584,	0.13571),
         (0.001668548584,	0.13465),
         (0.002224731445,	0.1899),
         (0.002224731445,	0.18948),
         (0.002966308594,	0.2575),
         (0.002966308594,	0.25752),
         (0.003955078125,	0.35383),
         (0.003955078125,	0.35256),
         (0.0052734375,	0.4755),
         (0.0052734375,	0.47219),
         (0.010546875,	1.0199),
         (0.010546875,	1.0106),
         (0.02109375,	2.1748),
         (0.02109375,	2.17243)]
mse = partial(square_eror, table)
cur_sq = grad_descent(mse)
print("r2=",cur_sq[0]," a=",cur_sq[1])