N, M = map(int, input().split())

from itertools import combinations
combs = combinations([i for i in range(1, N + 1)], M)
for comb in combs:
    print(" ".join(map(str, list(comb))))