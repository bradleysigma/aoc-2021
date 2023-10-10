import aoc
from collections import defaultdict

data = aoc.strlist(21)

r = [int(i.split(" ")[-1]) for i in data]
p = {tuple(r) + (0, 0): 1}

s = [0, 0]
d = 0
while max(s) < 1000:
    r[d%2] = (r[d%2]+3*d+5)%10 + 1
    s[d%2] += r[d%2]
    d += 3

g = [0,0]
for n in range(20):
    q = defaultdict(int)
    for (a, b, u, v), t in p.items():
        if max(u, v) >= 21:
            g[n%2] += t
            continue
        for i, j in [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]:
            q[(a, (b+i-1)%10 + 1, u, v + (b+i-1)%10 + 1) if n%2 else ((a+i-1)%10 + 1, b, u + (a+i-1)%10 + 1, v)] += j*t
    p = q

print(min(s) * d, max(g))
