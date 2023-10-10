import aoc
from collections import defaultdict

data = aoc.strgroups(19)

p = dict(enumerate(map(lambda y: set(map(lambda x: aoc.vec(map(int, x.split(","))), y[1:])), data)))
q = {i: set([aoc.vec.zero(3)]) for i in p.keys()}
m = defaultdict(dict)
f = [(lambda i, j, k: lambda x, y, z: k * i * ((x, y, z)[j:]+(x, y, z)[0:j])[::k])(i, j, k) for k in (-1, 1) for j in range(3) for i in (aoc.vec((u, v, u*v)) for u in (-1, 1) for v in (-1, 1))]
g = [min(j for j in f if i(*j(1, 2, 3)) == aoc.vec((1, 2, 3))) for i in f]

for i in range(len(p)):
    for j in range(i):
        for k in range(len(f)):
            d = defaultdict(int)
            for u in p[i]:
                for v in p[j]:
                    d[u-f[k](*v)] += 1
            if max(d.values()) == 12:
                m[i][j] = (max(d, key=d.get), f[k])
                m[j][i] = (-g[k](*max(d, key=d.get)), g[k])
                break
aoc.tock()
w = []
s = {0}
while s:
    i = s.pop()
    for j in filter(lambda x: all(k[1] != x and (x, i) != k for k in w), m[i]):
        w.append((i, j))
        s.add(j)

for i, j in w[::-1]:
    h, r = m[i][j]
    p[i] |= set(r(*b) + h for b in p[j])
    q[i] |= set(r(*b) + h for b in q[j])

print(len(p[0]), max((i-j).manhattan() for i in q[0] for j in q[0]))
