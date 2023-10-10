import aoc
from collections import defaultdict

data = aoc.strgroups(20)

a = data[0][0]
p = defaultdict(lambda: ".", {(i,j): data[1][j][i] for j in range(len(data[1])) for i in range(len(data[1][j]))})

y = {}
for n in range(50):
    r = range(min(k[0] for k in p)-1, max(k[0] for k in p)+2)
    p = defaultdict(lambda: (a[-1]+a[0])[n%2], {(i,j): a[sum(2**(4-u-3*v)*(p[i+u, j+v] == "#") for v in [-1,0,1] for u in [-1,0,1])] for j in range(min(k[1] for k in p)-1, max(k[1] for k in p)+2) for i in r})
    y[n+1] = "".join(p.values()).count("#")

print(y[2], y[50])
