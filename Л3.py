from sys import stdin
from itertools import combinations

def is_set(l, m ,n):
    global tr
    if not(tuple(l) in tr) and not(tuple(m) in tr) and not(tuple(n) in tr):
        b = is_congr(l[0], m[0], n[0]) and is_congr(l[1], m[1], n[1])
        if b:
            tr = tr | {tuple(l), tuple(m) , tuple(n)}
        return b
    return False
def is_congr(l,m,n):
    return (l != m) and (n != m) and (l != n) or (l == m) and (n == m) and (l == n)

tr = set()
cor = list()
allp = list()
n = int(input())
for i, line in enumerate(stdin,1):
    line = line.split()
    m = line + [i]
    for j,k in combinations(allp, 2):
        if is_set(j,k,m):
            cor.append(f'{j[2]} {k[2]} {i}')
    allp.append(m)

print('\n'.join(cor))