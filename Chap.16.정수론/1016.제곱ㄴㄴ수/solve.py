def solve(n, m):
    sieve = [1] * (m - n + 1)
    for k in range(2, int(m ** 0.5) + 1):
        s = k * k
        i = 0 if n % s == 0 else s - (n % s)
        for t in range(i, len(sieve), s):
            sieve[t] = 0
    return sum(sieve)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
print(solve(n, m))