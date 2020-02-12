class EratosthenesGood:
    prim_list = [2,3]

    def __init__(self):
        self.prim_list = EratosthenesGood.prim_list
    def prim(self, x):
        xs = [i for i in range(self.prim_list[- 1] + 1, x + 1)]
        for j in self.prim_list + xs:
            for i in xs[::-1]:
                if i <= j:
                    break
                if (i % j == 0):
                    xs.remove(i)
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
        EratosthenesGood.prim_list = self.prim_list
        return res
e = EratosthenesGood()
print (e.is_prime(4))
print (e.is_prime(1000))
print (EratosthenesGood().prim_list)