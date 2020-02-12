import time
import datetime


class EratosthenesGood():
    def __init__(self, x, prost):
        self.x = x
        self.prost = prost


X = 10000000
y1 = EratosthenesGood(2, True)
xs = [y1]
for i in range(3, X + 1):
    y = EratosthenesGood(i, True)
    xs.append(y)

for i in range(2, X):
    for j in range(i * 2, X, i):
        if ((xs[j - 2].x) % i == 0):
            xs[j - 2].prost = False
        if j % (X - 1) == 0:
            print(time.clock(), '  ', i)

"""for i in range(0, X - 1):
    print(xs[i].x, xs[i].prost)"""

print(time.clock())

while (True):
    A = int(input())
    print(xs[A - 2].prost)
