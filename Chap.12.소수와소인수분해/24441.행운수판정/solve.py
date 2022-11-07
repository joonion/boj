def solve(n):
    p = 2
    while p <= n:
        if n % p != 0:
            n -= n // p
            p += 1
        else:
            return False
    return True

def lucky_number(n):
    sieve = [i for i in range()]

import sys
input = sys.stdin.readline
sieve = lucky_number(10**6)
T = int(input())
for i in range(T):
    n = int(input())
    print(n, "lucky" if n in sieve else "unlucky")
