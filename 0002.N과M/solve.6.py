N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

from itertools import combinations
combs = combinations(nums, M)
for comb in combs:
    print(" ".join(map(str, list(comb))))