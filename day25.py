import aoc

data = aoc.strlist(25)

p = [list(i) for i in data]
n = len(p)
m = len(p[0])
b = True
y = 0

while b:
    y += 1
    b = False

    q = [m*["."] for j in range(n)]
    for u in range(n):
        for v in range(m):
            if p[u][v] == ">" and p[u][(v+1)%m] == ".":
                q[u][(v+1)%m] = ">"
                b = True
            elif p[u][v] != ".":
                q[u][v] = p[u][v]
    p = q
    
    q = [m*["."] for j in range(n)]
    for u in range(n):
        for v in range(m):
            if p[u][v] == "v" and p[(u+1)%n][v] == ".":
                q[(u+1)%n][v] = "v"
                b = True
            elif p[u][v] != ".":
                q[u][v] = p[u][v]
    p = q

print(y)
