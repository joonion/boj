from itertools import permutations

def solve(n, m, nums):
    perms = permutations(nums, m)
    S = set()
    for perm in perms:
        S.add(perm)
    L = sorted(list(S))
    for e in L:
        print(" ".join(map(str, e)))

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
solve(n, m, nums)

