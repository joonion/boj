def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def larger(n):
    while True:
        n += 1
        if is_prime(n):
            return n

def smaller(n):
    while True:
        n -= 1
        if is_prime(n):
            return n
        
def solve(n):
    if is_prime(n):
        return 0
    else:
        return larger(n) - smaller(n)
    
T = int(input())
for _ in range(T):
    k = int(input())
    print(solve(k))