def find_primes(n):
    sieve = [0, 0] + [1] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
    return sieve
    
def solve(n, sieve):
    mindiff, mini, minj = 10**5, 0, 0
    for i in range(2, n // 2 + 1):
        if sieve[i] == 1 and sieve[n - i] == 1:
            if n - 2*i < mindiff:
                mindiff, mini, minj = n - 2*i, i, n - i 
    print(mini, minj)

sieve = find_primes(10000)
T = int(input())
for _ in range(T):
    n = int(input())
    solve(n, sieve)