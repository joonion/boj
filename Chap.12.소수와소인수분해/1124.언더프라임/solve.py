def num_factor(n):
    if n <= 1: return 0
    cnt = 0
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            cnt += 1
            n //= i
    cnt += n != 1
    return cnt
    
def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def is_underprime(n):
    return is_prime(num_factor(n))

def solve(n, m):
    cnt = 0
    for i in range(n, m + 1):
        cnt += is_underprime(i)
    return cnt

A, B = map(int, input().split())
print(solve(A, B))