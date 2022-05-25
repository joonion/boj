from math import floor, sqrt

def solve(m, n):
    sieve = [1] * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, floor(sqrt(n)) + 1):
        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
    for i in range(m, n + 1):
        if sieve[i] == 1:
            print(i)
    
M, N = map(int, input().split())
solve(M, N)
