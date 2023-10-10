import aoc

data = aoc.strlist(18)

def parse(s):
    if s.isnumeric():
        return int(s)
    k = min(i for i in range(len(s)) if s[1:i].count("[") == s[1:i].count("]") and s[i] == ",")
    return [parse(s[1:k]), parse(s[k+1:-1])]

def build(d, t=None, n=1):
    t = {} if t is None else t
    p, q = d
    if type(p) == int:
        t[2*n] = p
    else:
        build(p, t, 2*n)
    if type(q) == int:
        t[2*n+1] = q
    else:
        build(q, t, 2*n+1)
    return t

def explode(t):
    i = min(filter(lambda x: x>=32, t), default=None)
    if i is None:
        return False
    for j in range(i-2, 30, -2):
        while j:
            if j in t:
                t[j] += t[i]
                j = -1
                break
            j //= 2
        if j == -1:
            break
    for j in range(i+2, 64, 2):
        while j:
            if j in t:
                t[j] += t[i+1]
                j = -1
                break
            j //= 2
        if j == -1:
            break
    del t[i]
    del t[i+1]
    t[i//2] = 0
    return True

def split(t):
    for i in range(16, 32):
        while i > 1:
            if i in t and t[i] >= 10:
                t[2*i] = t[i] // 2
                t[2*i+1] = t[i] - t[2*i]
                del t[i]
                return True
            i = i//2 if i%2 else -1
    return False

def reduce(t):
    while explode(t) or split(t):
        pass
    return t

def join(u, v):
    return {i + (2 if i < 4 else 4 if i < 8 else 8 if i < 16 else 16): u[i] for i in u} | {j + (4 if j < 4 else 8 if j < 8 else 16 if j < 16 else 32): v[j] for j in v}

def mag(t, n=1):
    return t[n] if n in t else 3*mag(t, 2*n) + 2*mag(t, 2*n+1)

t = reduce(build(parse(data[0])))
for i in data[1:]:
    t = reduce(join(t, build(parse(i))))

print(mag(t), max(mag(reduce(join(build(parse(i)), build(parse(j))))) for i in data for j in data))
