from time import time

t = time()


def tock(units="s"):
    print(f'{(time() - t) * {"h": 1/3600, "m": 1/60, "s": 1, "ms": 1000, "us": 1e6}[units]:.2f}{units}')


def read(n):
    with open(f"input{n}.txt") as f:
        return f.read().strip("\n")


def strlist(n, t=list, d="\n"):
    return t(read(n).split(d))


def intlist(n, t=list, d="\n"):
    if d == "":
        return t(map(int, read(n)))
    return t(map(int, read(n).split(d)))


def strgroups(n, t=list):
    return t(i.split("\n") for i in read(n).split("\n\n"))

def intgrid(n, t=list):
    return t(map(lambda x: t(map(int, x)), read(n).split("\n")))


class vec(tuple):
    def __abs__(self):
        return tuple(abs(i) for i in self)

    def __add__(self, other):
        if isinstance(other, (int, float, complex)):
            return vec(i + other for i in self)
        if isinstance(other, (vec, tuple, list)):
            if len(self) != len(other):
                raise IndexError(f"iterable lengths mismatched ({len(self) - len(other)})")
            return vec(i + j for i, j in zip(self, other))
        if isinstance(other, (map, reversed, range)):
            return self + vec(other)
        raise TypeError(f"cannot add {type(other).__name__} to vec")

    def __radd__(self, other):
        return self + other

    def __bool__(self):
        return any(self)

    def __ceil__(self):
        return vec(i.__ceil__() for i in self)

    def __divmod__(self, other):
        if isinstance(other, (int, float, complex)):
            return vec(i // other for i in self), vec(i % other for i in self)
        if isinstance(other, (vec, tuple, list)):
            if len(self) != len(other):
                raise IndexError(f"iterable lengths mismatched ({len(self) - len(other)})")
            return vec(i // j for i, j in zip(self, other)), vec(i % j for i, j in zip(self, other))
        if isinstance(other, (map, reversed, range)):
            return divmod(self, vec(other))
        raise TypeError(f"cannot divmod {type(other).__name__} with vec")

    def __rdivmod__(self, other):
        if isinstance(other, (int, float, complex)):
            return vec(other // i for i in self), vec(other % i for i in self)
        if isinstance(other, (vec, tuple, list)):
            if len(self) != len(other):
                raise IndexError(f"iterable lengths mismatched ({len(self) - len(other)})")
            return vec(j // i for i, j in zip(self, other)), vec(j % i for i, j in zip(self, other))
        if isinstance(other, (map, reversed, range)):
            return divmod(vec(other), self)
        raise TypeError(f"cannot right divmod {type(other).__name__} with vec")

    def __eq__(self, other):
        if isinstance(other, vec):
            if len(self) != len(other):
                return False
            return all(i == j for i, j in zip(self, other))
        return False

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if isinstance(other, (int, float, complex)):
            return all(i > other for i in self)
        if isinstance(other, (vec, tuple, list)):
            if len(self) != len(other):
                raise IndexError(f"iterable lengths mismatched ({len(self) - len(other)})")
            return all(i > j for i, j in zip(self, other))
        if isinstance(other, (map, reversed, range)):
            return self > vec(other)
        raise TypeError(f"cannot > {type(other).__name__} with vec")

    def __ge__(self, other):
        if isinstance(other, vec):
            return self > other or self == other
        return False

    def __lt__(self, other):
        if isinstance(other, (int, float, complex)):
            return all(i < other for i in self)
        if isinstance(other, (vec, tuple, list)):
            if len(self) != len(other):
                raise IndexError(f"iterable lengths mismatched ({len(self) - len(other)})")
            return all(i < j for i, j in zip(self, other))
        if isinstance(other, (map, reversed, range)):
            return self < vec(other)
        raise TypeError(f"cannot < {type(other).__name__} with vec")

    def __le__(self, other):
        if isinstance(other, vec):
            return self < other or self == other
        return False

    def __floor__(self):
        return vec(i.__floor__() for i in self)

    def __floordiv__(self, other):
        if isinstance(other, (int, float, complex)):
            return vec(i // other for i in self)
        if isinstance(other, (vec, tuple, list)):
            if len(self) != len(other):
                raise IndexError(f"iterable lengths mismatched ({len(self) - len(other)})")
            return vec(i // j for i, j in zip(self, other))
        if isinstance(other, (map, reversed, range)):
            return self // vec(other)
        raise TypeError(f"cannot floordiv {type(other).__name__} to vec")

    def __rfloordiv__(self, other):
        if isinstance(other, (int, float, complex)):
            return vec(other // i for i in self)
        if isinstance(other, (vec, tuple, list)):
            if len(self) != len(other):
                raise IndexError(f"iterable lengths mismatched ({len(self) - len(other)})")
            return vec(j // i for i, j in zip(self, other))
        if isinstance(other, (map, reversed, range)):
            return vec(other) // self
        raise TypeError(f"cannot right floordiv {type(other).__name__} to vec")

    def __hash__(self):
        return hash(tuple(self))

    def __mod__(self, other):
        if isinstance(other, (int, float, complex)):
            return vec(i % other for i in self)
        if isinstance(other, (vec, tuple, list)):
            if len(self) != len(other):
                raise IndexError(f"iterable lengths mismatched ({len(self) - len(other)})")
            return vec(i % j for i, j in zip(self, other))
        if isinstance(other, (map, reversed, range)):
            return self % vec(other)
        raise TypeError(f"cannot modulo {type(other).__name__} with vec")

    def __rmod__(self, other):
        if isinstance(other, (int, float, complex)):
            return vec(other % i for i in self)
        if isinstance(other, (vec, tuple, list)):
            if len(self) != len(other):
                raise IndexError(f"iterable lengths mismatched ({len(self) - len(other)})")
            return vec(j % i for i, j in zip(self, other))
        if isinstance(other, (map, reversed, range)):
            return vec(other) % self
        raise TypeError(f"cannot right modulo {type(other).__name__} with vec")

    def __mul__(self, other):
        if isinstance(other, (int, float, complex)):
            return vec(i * other for i in self)
        if isinstance(other, (vec, tuple, list)):
            if len(self) != len(other):
                raise IndexError(f"iterable lengths mismatched ({len(self) - len(other)})")
            return vec(i * j for i, j in zip(self, other))
        if isinstance(other, (map, reversed, range)):
            return self * vec(other)
        raise TypeError(f"cannot multiply {type(other).__name__} to vec")

    def __rmul__(self, other):
        return self * other

    def __neg__(self):
        return vec(-i for i in self)

    def __pos__(self):
        return self

    def __pow__(self, other):
        if isinstance(other, (int, float, complex)):
            return vec(i ** other for i in self)
        if isinstance(other, (vec, tuple, list)):
            if len(self) != len(other):
                raise IndexError(f"iterable lengths mismatched ({len(self) - len(other)})")
            return vec(i ** j for i, j in zip(self, other))
        if isinstance(other, (map, reversed, range)):
            return self ** vec(other)
        raise TypeError(f"cannot exponentiate {type(other).__name__} with vec")

    def __rpow__(self, other):
        if isinstance(other, (int, float, complex)):
            return vec(other ** i for i in self)
        if isinstance(other, (vec, tuple, list)):
            if len(self) != len(other):
                raise IndexError(f"iterable lengths mismatched ({len(self) - len(other)})")
            return vec(j ** i for i, j in zip(self, other))
        if isinstance(other, (map, reversed, range)):
            return vec(other) ** self
        raise TypeError(f"cannot right exponentiate {type(other).__name__} with vec")

    def __round__(self):
        return vec(map(round, self))

    def __sub__(self, other):
        if isinstance(other, (int, float, complex)):
            return vec(i - other for i in self)
        if isinstance(other, (vec, tuple, list)):
            if len(self) != len(other):
                raise IndexError(f"iterable lengths mismatched ({len(self) - len(other)})")
            return vec(i - j for i, j in zip(self, other))
        if isinstance(other, (map, reversed, range)):
            return self - vec(other)
        raise TypeError(f"cannot subtract {type(other).__name__} to vec")

    def __rsub__(self, other):
        return -(self - other)

    def __truediv__(self, other):
        if isinstance(other, (int, float, complex)):
            return vec(i / other for i in self)
        if isinstance(other, (vec, tuple, list)):
            if len(self) != len(other):
                raise IndexError(f"iterable lengths mismatched ({len(self) - len(other)})")
            return vec(i / j for i, j in zip(self, other))
        if isinstance(other, (map, reversed, range)):
            return self / vec(other)
        raise TypeError(f"cannot divide {type(other).__name__} to vec")

    def __rtruediv__(self, other):
        if isinstance(other, (int, float, complex)):
            return vec(other / i for i in self)
        if isinstance(other, (vec, tuple, list)):
            if len(self) != len(other):
                raise IndexError(f"iterable lengths mismatched ({len(self) - len(other)})")
            return vec(j / i for i, j in zip(self, other))
        if isinstance(other, (map, reversed, range)):
            return vec(other) / self
        raise TypeError(f"cannot right divide {type(other).__name__} to vec")

    def __trunc__(self):
        return vec(i.__trunc__() for i in self)

    def as_integer_ratio(self):
        return vec(i.as_integer_ratio()[0] for i in self), vec(i.as_integer_ratio()[1] for i in self)

    def conjugate(self):
        return vec(i.conjugate() for i in self)

    def imag(self):
        return vec(i.imag for i in self)

    def real(self):
        return vec(i.real for i in self)

    def euclidean(self):
        return sum(i**2 for i in self)**0.5

    def manhattan(self):
        return sum(abs(self))

    def dot(self, *others):
        p = vec(self)
        for i in others:
            if isinstance(i, (int, float, complex)):
                raise TypeError("cannot dot product with scalar")
            p *= i
        return sum(p)

    def cross(self, *others):
        if len(self) != len(others) + 2:
            raise TypeError(f"vec.cross requires {len(self)-2} additional arugment{'s' if len(self)-2 != 1 else ''} for a {len(self)} length vec")
        for i in others:
            if len(i) != len(self):
                raise IndexError(f"iterable lengths mismatched ({len(self) - len(i)})")

        def det(m):
            if len(m) == 2:
                return m[0][0] * m[1][1] - m[0][1] * m[1][0]
            d = 0
            for i in range(len(m)):
                n = []
                for j in range(1, len(m)):
                    r = []
                    for k in [kk for kk in range(len(m)) if kk != i]:
                        r.append(m[j][k])
                    n.append(r)
                d += (1 if i % 2 == 0 else -1) * m[0][i] * det(n)
            return d
        if len(self) == 2:
            return vec([self[1], -self[0]])
        v = []
        for i in range(len(self)):
            m = []
            for j in range(len(self) - 1):
                r = []
                for k in [kk for kk in range(len(self)) if kk != i]:
                    r.append(((self,) + others)[j][k])
                m.append(r)
            v.append((1 if i % 2 == 0 else -1) * det(m))
        return vec(v)

    def unit(self):
        return vec(i / self.euclidean() for i in self)

    def triple(self, left, right):
        if any(len(i) != 3 for i in [self, left, right]):
            raise IndexError("triple product requires three 3d vectors")
        return self.dot(vec(left).cross(right))

    @classmethod
    def zero(cls, n):
        return cls(n * (0,))
