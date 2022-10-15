from math import floor, sqrt

def factorize(n):
    if n == 1:
        return []
    else:
        for i in range(2, floor(sqrt(n)) + 1):
            if n % i == 0:
                return [i] + factorize(n // i)
        return [n]
        
def solve(n):
    factors = factorize(n)
    for i in range(len(factors)):
        print(factors[i])

N = int(input())
solve(N)