def f(a, b, c, x):
    return a * (x**2) + b * x + c

def solve(a, b, c, n):
    if f(a, b, c, n) > 0 or a > 0:
        return False
    if a == 0 and b > 0:
        return False
    if a < 0:
        px = -b / (2 * a)
        if n <= px and f(a, b, c, px) > 0:
                return False
    return True

a, b, c, d, n = map(int, open(0).read().split())
print(1 if solve(a - d, b, c, n) else 0)