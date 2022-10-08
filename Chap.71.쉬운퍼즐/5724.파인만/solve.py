def solve(n):
    s = 0
    for k in range(n):
        s += (n - k) ** 2
    return s

while True:
    n = int(input())
    if n == 0: break
    print(solve(n))
