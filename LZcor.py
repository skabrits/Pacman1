from sys import stdin
from itertools import combinations

def is_set(l, m ,n):
    global tr
    b = is_congr(l[0], m[0], n[0]) and is_congr(l[1], m[1], n[1])
    if b:
        tr = tr | {l, m , n}
    return b
def is_congr(l,m,n):
    ch = {l,m,n}
    return not(len(ch) == 2)

tr = set()
cor = list()
allp = list()
n = int(input())
for i, line in enumerate(stdin,1):
    line = line.split()
    m = tuple(line + [i])
    for j in allp:
        if not(j in tr):
            for k in allp[:allp.index(j)]:
                if not (k in tr):
                    if is_set(j,k,m):
                        cor.append(f'{j[2]} {k[2]} {i}')
    allp.append(m)

print('\n'.join(cor))