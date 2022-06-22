def coord(a):
    return a % 4, a // 4

n, m = map(int, input().split())
x, y = coord(n - 1)
p, q = coord(m - 1)
print(abs(x - p) + abs(y - q))