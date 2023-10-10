import aoc
from collections import defaultdict

data = aoc.strlist(12)
d = defaultdict(list)
p = []
u = set()
for i, j in map(lambda x: x.split("-"), data):
    if i == "start":
        p.append([j])
    elif j == "start":
        p.append([i])
    elif i == "end":
        u.add(j)
    elif j == "end":
        u.add(i)
    else:
        d[i].append(j)
        d[j].append(i)
q = list(p)

n = 0
while p:
    i = p.pop()
    if i[-1] in u:
        n += 1
    for j in d[i[-1]]:
        if j.isupper() or j not in i:
            p.append(i + [j])

m = 0
while q:
    i = q.pop()
    if i[-1] in u:
        m += 1
    for j in d[i[-1]]:
        if j.isupper() or j not in i or all(i.count(k) != 2 or k.isupper() for k in i):
            q.append(i + [j])

print(n, m)
