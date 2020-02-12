from copy import copy
from math import sqrt
import pandas as pd
from numpy import NaN, Inf, log

M, SIG, S, G, RO = (0.1, 0.0001, 0.01, 10, 1000)
dr0 = 0.0000001
r0 = 0.0000001
def ddr(t):
    return ((SIG**2 * G**2 * M)/S**2 + dr0**2*RO*G - (SIG**2 * G * M * r0)/S**2)/(2*M*dr0)
def dr(t):
    dt = 0.0000001
    return dr0+ddr(t)*dt
def r(t):
    dt = 0.0000001
    return r0+dr(t)*dt
points = list()
for t in range(1,80000):
    tr = t/10000000
    points.append((r(tr), ddr(tr)))
    dr0 = dr(tr)
    r0 = r(tr)
print(points)
poi = pd.Series(list([point[1] for point in points if points[1] != NaN and points[1] != Inf]), list([point[0] for point in points if points[1] != NaN and points[1] != Inf]))
print(poi)
poi.plot.line()
import matplotlib.pyplot as plt
plt.show()
print(poi[0.00001])