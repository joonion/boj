N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

from itertools import combinations_with_replacement
combs = combinations_with_replacement(nums, M)
for comb in combs:
    print(" ".join(map(str, list(comb))))