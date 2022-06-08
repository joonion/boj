def solve(n, m):
    s = 0
    for i in range(n, m + 1):
        s += bin(i).count("1")
    return s

n, m = map(int, input().split())
print(solve(n, m))
