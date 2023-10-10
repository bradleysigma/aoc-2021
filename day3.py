import aoc

data = aoc.strlist(3)

n = len(data[0])
r = int("".join(max("01", key=lambda x: [i[j] for i in data].count(x)) for j in range(n)), 2)
print(r*(r^int(n*"1", 2)))

oxy = data
co2 = data
f = lambda t, s, c, j: list(filter(lambda x: x[j] == c(s, key=lambda x: [i[j] for i in t].count(x)), t))
for j in range(n):
    oxy = f(oxy, "10", max, j)
    if len(co2) > 1:
        co2 = f(co2, "01", min, j)
print(int(min(oxy), 2) * int(min(co2), 2))
