N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

from itertools import product
perms = product(nums, repeat = M)
for perm in perms:
    print(" ".join(map(str, list(perm))))