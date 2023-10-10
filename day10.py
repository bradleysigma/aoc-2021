import aoc
data = aoc.strlist(10)

n = 0
m = []
for i in data:
    t = len(i) + 1
    while len(i) < t:
        t = len(i)
        i = i.replace("()", "").replace("{}", "").replace("[]", "").replace("<>", "")
    s = []
    for j in i:
        if j in "}])>":
            n += {")": 3, "]": 57, "}": 1197, ">": 25137}[j]
            break
        s.append(" ([{<".find(j))
    else:
        m.append(sum(s[k]*5**k for k in range(len(s))))

print(n, sorted(m)[len(m)//2])
