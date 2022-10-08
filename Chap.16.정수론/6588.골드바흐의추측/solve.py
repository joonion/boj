def find_primes(n):
    sieve = [0, 0] + [1] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
    return sieve
    
def solve(n, sieve):
    for i in range(2, n // 2 + 1):
        if sieve[i] == 1 and sieve[n - i] == 1:
            print(f"{n} = {i} + {n-i}")
            return

sieve = find_primes(1000000)
while True:
    n = int(input())
    if n == 0: break
    solve(n, sieve)