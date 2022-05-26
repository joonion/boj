N, M = map(int, input().split())

from itertools import combinations_with_replacement
combs = combinations_with_replacement([i for i in range(1, N+1)], M)
for comb in combs:
    print(" ".join(map(str, list(comb))))