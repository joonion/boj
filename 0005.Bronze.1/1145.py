from math import lcm
from itertools import combinations

A = list(map(int, input().split()))
combs = combinations(A, r = 3)
opt = 100**3
for comb in combs:
    opt = min(opt, lcm(*comb))
print(opt)