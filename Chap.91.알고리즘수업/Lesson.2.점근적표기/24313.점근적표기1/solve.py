def solve(a1, a0, c, n0):
    f = a1 * n0 + a0
    g = c * n0
    return f <= g and a1 <= c

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())
print(1 if solve(a1, a0, c, n0) else 0)
