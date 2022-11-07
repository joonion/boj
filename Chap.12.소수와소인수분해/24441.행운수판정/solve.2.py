import math 

def solve(n, k):
    if n < k:
        return True
    elif n % k == 0:
        return False
    else:
        n -= n / k
        return solve(n, k + 1)

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    print(n, "lucky" if solve(n, 2) else "unlucky")
