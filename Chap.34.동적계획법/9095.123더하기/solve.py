def solve(n):
    if n < 3:
        return n
    elif n == 3:
        return 4
    else:
        D = [0] * (n + 1)
        D[1], D[2], D[3] = 1, 2, 4
        for i in range(4, n + 1):
            D[i] = D[i - 1] + D[i - 2] + D[i - 3]
        return D[n]

T = int(input())
for _ in range(T):
    n = int(input())
    print(solve(n))