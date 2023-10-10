import aoc

data = aoc.intlist(7, d=",")
##m = 10**9
##n = 10**9
##
##for i in range(min(data), max(data)+1):
##    m = min(m, sum(abs(j-i) for j in data))
##    n = min(n, sum(abs(j-i)*(abs(j-i)+1)//2 for j in data))
##print(m, n)


print(sum(abs(j-sorted(data)[len(data)//2]) for j in data),
      sum((lambda x: x*(x+1)//2)(abs(j-sum(data)//len(data))) for j in data))
