import aoc
from collections import defaultdict
data = aoc.strlist(14)

s = data[0]
d = {(i,j): t for (i,j), t in map(lambda x: x.split(" -> "), data[2:])}
f = set(d.values())

p = defaultdict(int)
for i,j in zip(s, s[1:]):
    p[i,j] += 1

for m in [10, 30]:
    for n in range(m):
        q = defaultdict(int)
        for i,j in p:
            q[i,d[i,j]] += p[i,j]
            q[d[i,j],j] += p[i,j]
        p = q

    r = [sum(p.get((i,j), 0) for j in f) + (i == s[-1]) for i in f]
    print((max(r) - min(r)))
