from itertools import permutations
a = 0
for i in permutations((True,)*10+(False,)*10, 10):
    (x1, x2, x3, x4, x5, x6, x7, x8, x9, x10) = i
    if ((x1 == x2) or (x3 == x4)) and (((x1 == x2) or (x3 == x4))) and ((x5 == x6) or (x7 == x8)) and (((x5 == x6) or (x7 == x8))) and ((x1 == x2) or (x7 == x8)) and (((x1 == x2) or (x7 == x8))) and ((x5 == x6) or (x3 == x4)) and (((x5 == x6) or (x3 == x4))) and (x9 == x10):
        a = a + 1
print(a)