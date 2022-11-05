def solve(N, S):
    for i in range(N):
        for j in range(N):
            if i != j:
                s = S[i] + S[j]
                if s == s[::-1]:
                    print(s)
                    return
    print(0)

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    S = [input().strip() for _ in range(N)]
    solve(N, S)
