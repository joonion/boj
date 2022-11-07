def find_primes(n):
    sieve = [0, 0] + [1] * (n - 1)
    for i in range(2, int(n**0.5) + 1):
        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
    primes = []
    for i in range(len(sieve)):
        if sieve[i]: primes.append(i)
    return primes

def solve(n, primes):
    cnt = 0
    for i in range(len(primes)):
        if primes[i] > n: break
        for j in range(i, len(primes)):
            if primes[j] > n: break
            for k in range(j, len(primes)):
                if primes[k] > n: break
                if primes[i] + primes[j] + primes[k] == n:
                    cnt += 1
    return cnt

primes = find_primes(1000000)
T = int(input())
for _ in range(T):
    N = int(input())
    print(solve(N, primes))
