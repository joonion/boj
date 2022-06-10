def findprimes(n):
    sieve = [0, 0] + [1] * (n - 1)
    for i in range(2, int(n**0.5) + 1):
        for j in range(i * i, n + 1, i):
            sieve[j] = 0
    primes = [0]
    for i in range(2, n + 1):
        if sieve[i] == 1:
            primes.append(primes[-1] + i)
    return primes
    
def solve(n):
    primes = findprimes(n)
    cnt = 0
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            S = primes[j] - primes[i]
            if S >= n:
                if S == n: cnt += 1
                break
    return cnt
        
n = int(input())
print(solve(n))