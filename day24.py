import aoc
from itertools import product

data = aoc.strlist(24)

a = list(map(lambda x: int(x.split(" ")[-1]), data[4::18]))
b = list(map(lambda x: int(x.split(" ")[-1]), data[5::18]))
c = list(map(lambda x: int(x.split(" ")[-1]), data[15::18]))

s = []
p = []
for i in range(14):
    if a[i] == 1:
        s.append(i)
    else:
        j = s.pop()
        p.append((j,i,c[j]+b[i]))

y = 14*[None]
for i,j,k in p:
    y[i] = 9 - (0 if k < 0 else k)
    y[j] = 9 + (k if k < 0 else 0)
print("".join(map(str,y)))

y = 14*[None]
for i,j,k in p:
    y[i] = 1 - (k if k < 0 else 0)
    y[j] = 1 + (0 if k < 0 else k)
print("".join(map(str,y)))
