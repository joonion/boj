def find_primes(n):
    sieve = [0, 0] + [1] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
    return sieve
    
def solve(n, sieve):
    cnt = 0
    for i in range(2, n // 2 + 1):
        if sieve[i] == 1 and sieve[n - i] == 1:
            cnt += 1
    return cnt

sieve = find_primes(1000000)
T = int(input())
for _ in range(T):
    n = int(input())
    print(solve(n, sieve))