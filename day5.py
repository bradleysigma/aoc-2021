import aoc
from collections import defaultdict

data = aoc.strlist(5)

d = defaultdict(int)
dd = defaultdict(int)

for i in data:
    x1, y1, _, x2, y2 = i.replace(" ", ",").split(",")
    x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
    (x1, y1), (x2, y2) = sorted([(x1, y1), (x2, y2)])
    if x1 == x2:
        for j in range(y1, y2+1):
            d[x1, j] += 1
    elif y1 == y2:
        for j in range(x1, x2+1):
            d[j, y1] += 1
    else:
        for j in range(x2-x1+1):
            dd[x1+j, y1+(j if y2 > y1 else -j)] += 1

print(sum(d[k] >= 2 for k in d), sum(d[k] + dd[k] >= 2 for k in set(d) | set(dd)))
