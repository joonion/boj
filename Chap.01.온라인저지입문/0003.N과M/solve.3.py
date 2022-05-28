N, M = map(int, input().split())

from itertools import product
perms = product([i for i in range(1, N + 1)], repeat = M)
for perm in perms:
    print(" ".join(map(str, list(perm))))