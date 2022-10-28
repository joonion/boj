def solve(a1, a0, c1, c2, n0):
    f = a1 * n0 + a0
    g1 = c1 * n0
    g2 = c2 * n0
    return g1 <= f <= g2 and c1 <= a1 <= c2

a2,a1, a0 = map(int, input().split())
c1, c2 = map(int, input().split())
n0 = int(input())
print(1 if solve(a1, a0, c1, c2, n0) else 0)
