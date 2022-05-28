N, M = map(int, input().split())

from itertools import permutations
perms = permutations([i for i in range(1, N + 1)], M)
for perm in perms:
    print(" ".join(map(str, list(perm))))

