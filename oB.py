from sys import stdin

pole = list()
val = list()
n,k = (0,0)
numb = 0
cou = True
for line in stdin:
    a = line.split(" ")
    if cou:
        cou = False
        n,k = map(int, tuple(a))
    else:
        pole.append(list(map(int,a)))
        val += [(int(a[0]),numb,0),(int(a[1]),numb,1)]
        numb += 1
val.sort()
val = val[::-1]
answ = list([0,0] for i in range(len(pole)))
for i in range(k):
    j = val[0][1]
    p = val[0][2]
    if pole[j][p]:
        aa = (pole[j][1],j,2 - p - 1)
        ab = (0,0)
        ac = (0,0)
        if(j - 1 >= 0):
            ab = (pole[j-1][0],j,p)
        if(j+1 < n):
            ac = (pole[j+1][0],j+1,p)
        itog = 0
        if (aa in val):
            itog += 1
        if (ab in val):
            itog += 10
        if (ac in val):
            itog += 100
        if itog == 0:
            val.pop(0)
        else:
            if itog == 1:
                m = aa
            elif itog == 10:
                 m = ab
            elif itog == 100:
                m = ac
            elif itog == 11:
                m = max(aa, ab)
            elif itog == 110:
                m = max(ab, ac)
            elif itog == 101:
                m = max(aa, ac)
            else:
                m = max(aa, ab, ac)
            print(m)
            print(j,p)
            answ[val[0][1]][val[0][2]] = i
            answ[m[1]][m[2]] = i
            val.remove(m)
            val.pop(0)
for i in answ:
    print(i)
