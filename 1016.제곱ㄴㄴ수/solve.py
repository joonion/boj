def solve(n, m):
    A = [1] * (m - n + 1)
    for k in range(2, int(m**0.5) + 1):
        s = k * k
        i = 0 if n % s == 0 else s - (n % s)
        for j in range(i, len(A), s):
            A[j] = 0
    return sum(A)

n, m = map(int, input().split())
print(solve(n, m))