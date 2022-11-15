def cut(n, s, h):
    length = 0
    for i in range(n):
        length += (s[i] - h) if s[i] > h else 0
    return length

def solve(n, M, s):
    low, high = 0, max(s)
    while low <= high:
        mid = (low + high) // 2
        if cut(n, s, mid) < M:
            high = mid - 1
        else:
            low = mid + 1
    return high

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = list(map(int, input().split()))
print(solve(N, M, S))