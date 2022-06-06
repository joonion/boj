from itertools import combinations_with_replacement

def solve(n, m, nums):
    combs = combinations_with_replacement(nums, m)
    S = set()
    for comb in combs:
        S.add(tuple(sorted(list(comb))))
    L = sorted(list(S))
    for e in L:
        print(" ".join(map(str, e)))

    
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
solve(n, m, nums)