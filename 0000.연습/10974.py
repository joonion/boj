from itertools import permutations
N = int(input())
perm = permutations([i for i in range(1, N + 1)], N)
for p in perm:
    print(" ".join(map(str, list(p))))