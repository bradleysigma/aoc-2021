import aoc
data = aoc.strlist(13)

p = {map(int, t.split(",")) for t in data[:data.index("")]}
for t in range(data.index("")+1, len(data)):
    d, n = data[t].split(" ")[-1].split("=")
    n = int(n)
    p = {(x, n-abs(y-n)) if d == "y" else (n-abs(x-n), y) for x, y in p}
    if data[t-1] == "":
        print(len(p))

print("\n".join("".join("#" if (i,j) in p else " " for i in range(1+max(k[0] for k in p))) for j in range(1+max(k[1] for k in p))))
