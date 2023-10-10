import aoc

data = aoc.read(17).strip()
xa, xb, ya, yb = map(int, filter(None, "".join(i if i in "0123456789-" else " " for i in data).split(" ")))

h = []
n = 0
for v in range(ya, -ya):
    for u in range(int(-0.5*((8*xa+1)**0.5+1)), xb+1):
        t = []
        for k in range(-2*ya+1):
            p = min(k,u)*u-min(k,u)*(min(k,u)-1)//2
            q = k*v-k*(k-1)//2
            t.append(q)
            if xa <= p <= xb and ya <= q <= yb:
                n += 1
                h.append(max(t))
                break
            if p > xb or q < ya:
                break
print(max(h), n)
