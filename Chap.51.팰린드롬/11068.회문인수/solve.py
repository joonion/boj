def base(n, b):
    s = []
    while n > 0:
        s.append(n % b)
        n //= b
    return s

def solve(n):
    for i in range(2, 65):
        s = base(n, i)
        if s == s[::-1]:
            return 1
    return 0

T = int(input())
for _ in range(T):
    N = int(input())
    print(1 if solve(N) else 0)
