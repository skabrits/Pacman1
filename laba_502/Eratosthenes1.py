import time
import datetime

class Eratosthenes:
    def __init__(self):
        self.prim_list = [2,3]
    def prim(self, x):
        xs = [i for i in range(self.prim_list[- 1] + 1, x + 1)]
        for j in self.prim_list + xs:
            for i in xs[::-1]:
                if i <= j:
                    break
                if (i % j == 0):
                    xs.remove(i)
                    print(time.clock(), '  ', i)
        self.prim_list += xs
        return self.find(x, -1)

    def find(self, x, a = 1):
        res = False
        for i in self.prim_list[::a]:
            if (i == x):
                res = True
        return res
    def is_prime(self, x):
        res = False
        if x > self.prim_list[len(self.prim_list) - 1]:
            res = self.prim(x)
        else:
            res = self.find(x)
        return res
e = Eratosthenes()
print (e.is_prime(1000000))
print(time.clock())