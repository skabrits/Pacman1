from sys import stdin
from itertools import combinations

tr = set()

def is_set(l, m ,n):
    global tr
    if not(tuple(l) in tr) and not(tuple(m) in tr) and not(tuple(n) in tr):
        b = is_congr(l[0], m[0], n[0]) and is_congr(l[1], m[1], n[1])
        if b:
            tr = tr | {tuple(l), tuple(m) , tuple(n)}
        return b
    else:
        return False
def is_congr(l,m,n):
    return (l != m) and (n != m) and (l != n) or (l == m) and (n == m) and (l == n)

n = int(input())
print('\n'.join(f'{l[2]} {n[2]} {m[2]}' for l,n,m in combinations([line.split()+[i] for i, line in enumerate(stdin,1) if len(line.split())>1], 3) if is_set(l, m ,n)))