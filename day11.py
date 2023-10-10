import aoc
data = aoc.intgrid(11)

f = []
while max(f + [-1]) != 100:
    data = [[x+1 for x in r] for r in data]
    while any(max(r) > 9 for r in data):
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] > 9:
                    data[i][j] = 0
                    for u, v in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                        if 0 <= i+u < len(data) and 0 <= j+v < len(data[i]) and data[i+u][j+v] != 0:
                            data[i+u][j+v] += 1
    f.append(sum(r.count(0) for r in data))

print(sum(f[:100]), len(f))
