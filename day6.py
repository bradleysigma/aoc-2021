import aoc
from collections import defaultdict

data = aoc.intlist(6, d=",")

d = defaultdict(int)
for i in data:
    d[i] += 1

for j in range(80):
    dd = defaultdict(int)
    for k in d:
        if k == 0:
            dd[6] += d[k]
            dd[8] += d[k]
        else:
            dd[k-1] += d[k]
    d = dd
print(sum(d.values()))

for j in range(80, 256):
    dd = defaultdict(int)
    for k in d:
        if k == 0:
            dd[6] += d[k]
            dd[8] += d[k]
        else:
            dd[k-1] += d[k]
    d = dd
print(sum(d.values()))
