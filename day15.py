import aoc
from collections import defaultdict

data = aoc.intgrid(15)

b = [list(j) for j in data] + [[] for k in range(4*len(data))]
for i in range(len(data)):
    b[i] += sum([[(j+k-1)%9+1 for j in b[i]] for k in [1,2,3,4]], [])
    for k in [1,2,3,4]:
        b[k*len(data)+i] = [(j+k-1)%9+1 for j in b[i]]

for m in [data, b]:
    d = defaultdict(lambda: 999999999)
    d[0,0] = 0
    r = defaultdict(lambda: 999999999)
    r[0,0] = 0
    s = [(0, 0)]
    p, q = len(m)-1, len(m[-1])-1
            

    while True:
        i, j = s.pop(0)
        if (i, j) == (p, q):
            print(d[i,j])
            break

        for u, v in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= u <= p and 0 <= v <= q and d[i,j] + m[u][v] < d[u,v]:
                d[u,v] = d[i,j] + m[u][v]
                r[u,v] = d[u,v] - i - j
                s.append((u,v))
        s.sort(key=r.get)
