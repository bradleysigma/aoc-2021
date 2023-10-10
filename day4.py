import aoc

data = aoc.strlist(4)

d = 5
w = True
calls = map(int, data[0].split(","))
boards = [[list(map(int, filter(None, j.split(" ")))) for j in data[i:i+d]] for i in range(2, len(data), d+1)]

while boards:
    c = next(calls)
    for i in range(len(boards)-1, -1, -1):
        b = boards[i]
        for j in range(d):
            for k in range(d):
                if b[j][k] == c:
                    b[j][k] = None

        if any(all(k is None for k in j) for j in b) or any(all(j[k] is None for j in b) for k in range(d)):
            if w or len(boards) == 1:
                print(c * sum(filter(None, sum(b, []))))
                w = False
            boards.pop(i)
