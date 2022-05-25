from math import floor, sqrt

def divisors(n):
    divs = []
    for i in range(1, floor(sqrt(n)) + 1):
        if n % i == 0:
            divs.append(i)
            if i * i != n:
                divs.append(n // i)
    return sorted(divs)    
        
def solve(n, k):
    divs = divisors(n)
    if len(divs) < k:
        return 0
    return divs[k - 1]

N, K = map(int, input().split())
answer = solve(N, K)
print(answer)