d, m = map(int, input().split())
D = list(map(int, input().split()))
M = list(map(int, input().split()))

from math import gcd, lcm
L = lcm(*D)
G = gcd(*M)

def divisor(n):
    div = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            div.add(i);
            div.add(n // i)
    return div
    
div = divisor(G)
cnt = 0
for k in div:
    if k % L == 0:
        cnt += 1
print(cnt)