def eratos(n):
    sieve = [0, 0] + [1] * (n - 1)
    sqrtn = int(n ** 0.5)
    for i in range(2, sqrtn + 1):
        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
    return sieve
    

def solve(n, sieve):
    cnt = 0
    for i in range()
    return cnt


import sys
input = sys.stdin.readline

T = int(input())
A = [int(input()) for _ in range(T)]
sieve = eratos(max(A))    
for i in range(T):
    print(solve(A[i], sieve))