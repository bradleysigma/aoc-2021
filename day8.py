import aoc
data = aoc.strlist(8)

n = 0
m = 0
for i in data:
    p, q = map(lambda x: ["".join(sorted(j)) for j in x.split(" ")], i.split(" | "))
    n += sum(len(j) in [2, 4, 3, 7] for j in q)
    d = {}

    for i in sorted(p, key=lambda x: len(x)**4%15):
        if len(i) == 6:
            if set(i).issuperset(d[4]):
                d[9] = i
            elif set(i).issuperset(d[1]):
                d[0] = i
            else:
                d[6] = i
        elif len(i) == 5:
            if set(i).issuperset(d[1]):
                d[3] = i
            elif set(i).issubset(d[6]):
                d[5] = i
            else:
                d[2] = i
        else:
            d[{2: 1, 3: 7, 4: 4, 7: 8}[len(i)]] = i

    m += int("".join(min(str(j) for j in d if d[j] == i) for i in q))
    
print(n, m)
