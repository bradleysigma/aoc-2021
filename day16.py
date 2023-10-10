import aoc
from math import prod

data = aoc.read(16).strip()

def parse(p):
    v = [int(p[:3], 2)]
    t = int(p[3:6], 2)
    if t == 4:
        return (v, int("".join(p[5*i+7:][:4] for i in range(p[6::5].index("0")+1)), 2), p[5*p[6::5].index("0")+11:])

    y = []
    if int(p[6]):
        n = int(p[7:18], 2)
        p = p[18:]
        for i in range(n):
            u, x, p = parse(p)
            y.append(x)
            v += u
    else:
        n = int(p[7:22], 2)
        q = p[22:22+n]
        while "1" in q:
            u, x, q = parse(q)
            y.append(x)
            v += u
        p = p[22+n:]

    return (v, [sum, prod, min, max, None, lambda k: k[0] > k[1], lambda k: k[0] < k[1], lambda k: k[0] == k[1]][t](y), p)

v, y, p = parse(bin(int(data, 16))[2:].rjust(4*len(data), "0"))
print(sum(v), y)
