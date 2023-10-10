import aoc
data = aoc.intgrid(9)

x = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if not any(0 <= i+u < len(data) and 0 <= j+v < len(data[i]) and data[i+u][j+v] <= data[i][j] for u, v in [(-1, 0), (1, 0), (0, -1), (0, 1)]):
            x += data[i][j]+1

m = {(i, j) for i in range(len(data)) for j in range(len(data[i])) if data[i][j] != 9}
y = []
while m:
    s = 1
    q = [m.pop()]
    while q:
        i, j = q.pop()
        for u, v in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= i+u < len(data) and 0 <= j+v < len(data[i]) and (i-u, j+v) in m:
                m.remove((i-u, j+v))
                q.append((i-u, j+v))
                s += 1
    y.append(s)

y.sort()
print(x, y[-3]*y[-2]*y[-1])
