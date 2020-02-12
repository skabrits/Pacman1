import numpy as np
import itertools
from functools import partial
import decimal

def grad_descent(func):

    def num_deriv(x):
        dx = 10 ** -10
        return [(func([x[0] + dx, x[1], x[2]]) - func(x)) / dx, (func([x[0], x[1] + dx, x[2]]) - func(x)) / dx, (func([x[0], x[1], x[2] + dx]) - func(x)) / dx]

    def find_local_min(x):
        delt = 10 ** -10
        i = 0
        while (max(map(abs, num_deriv(x))) >= delt and i < 10 ** 4):
            res_sum = 0
            nd = num_deriv(x)
            if x[0] - 0.1 * nd[0] > 0 and x[0] - 0.1 * nd[0] < 10000:
                x[0] = x[0] - 0.1 * nd[0]
            else:
                res_sum = res_sum + 1

            if x[1] - 0.05 * nd[1] > 0 and x[1] - 0.05 * nd[1] < 1000:
                x[1] = x[1] - 0.05 * nd[1]
            else:
                res_sum = res_sum + 1

            if x[2] - 0.01 * nd[2] > 0 and x[2] - 0.01 * nd[2] < 1:
                x[2] = x[2] - 0.01 * nd[2]
            else:
                res_sum = res_sum + 1

            if res_sum == 3:
                break

            i = i + 1
        return (func(x), x[0], x[1], x[2])

    arr_lm = [[(i * 800), (i * 100), (i / 10)] for i in range(0, 10)]
    m = min(list(map(find_local_min, arr_lm)))
    return tuple(m)

def square_eror(arr, tp):
    (a, b, n) = tp
    return sum([(y - ((x) ** (n + 1)) * a / (x + b)) ** 2 for x, y in arr])

def comb(arr):
    arr1 = list()
    for i in range(3, len(arr) + 1):
        for i in itertools.combinations(arr, i):
            arr1.append(i)
    return arr1

table = [(4, 930.5137966), (3.6, 4283.066598), (3.2, 5141.344719), (3.2, 1826.93911), (2.8, 1874.155317), (2.4, 1485.670611), (2, 1088.386168), (1.8, 1711.839526), (1.6, 694.2971419), (1.4, 1129.01216), (1.2, 1229.743192), (1, 1027.483882)]
table = table[::-1]
sq = list()
a1 = comb(table)
coun = 0
for arr in a1:
    square_erorm = partial(square_eror, arr)
    cur_sq = grad_descent(square_erorm)
    print(coun/len(a1) * 100)
    sq.append(cur_sq)
    coun += 1
optimal = min(sq)
print("r2=",optimal[0]," a=",optimal[1]," b=",optimal[2]," n=",optimal[3])
print(sq)