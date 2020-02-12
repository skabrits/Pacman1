from sympy.utilities.iterables import multiset_permutations

c = 0
n = int(input('number NxN'))
for i in multiset_permutations(('vnis',) * n + ('vlevo',) * n, n * 2):
    c = c + 1
print(c)