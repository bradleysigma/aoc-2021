import aoc
data = aoc.intlist(1)
print(sum(i < j for i, j in zip(data, data[1:])),
      sum(i < j for i, j in zip(data, data[3:])))
