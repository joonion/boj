N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

from itertools import permutations
perms = permutations(nums, M)
for perm in perms:
    print(" ".join(map(str, list(perm))))