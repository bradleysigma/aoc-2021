import aoc

data = aoc.strlist(2)
x, y, z = 0, 0, 0

for i in data:
    d, n = i.split(" ")
    n = int(n)
    if d == "forward":
        x += n
        z += n*y
    else:
        y += n if d == "down" else -n

print(x*y)
print(x*z)
