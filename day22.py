import aoc

def f(p):
    xap, xbp, yap, ybp, zap, zbp, cp = p[0]
    s = [(max(xaq, xap), min(xbq, xbp), max(yaq, yap), min(ybq, ybp), max(zaq, zap), min(zbq, zbp), cq) for xaq, xbq, yaq, ybq, zaq, zbq, cq in p[1:] if all([xbq > xap, xaq < xbp, ybq > yap, yaq < ybp, zbq > zap, zaq < zbp])]
    return (xbp-xap+1) * (ybp-yap+1) * (zbp-zap+1) - sum(f(s[i:]) for i in range(len(s)))

data = aoc.strlist(22)

r = [tuple(map(int, filter(None, "".join(j if j in "-0123456789" else " " for j in i).split()))) + (i[:2] == "on",) for i in data]
m = [f(r[i:]) * (1 if all(-50 <= j <= 50 for j in r[i][:-1]) else -1) for i in range(len(r)) if r[i][-1]]
print(sum(max(0, i) for i in m), sum(abs(i) for i in m))
