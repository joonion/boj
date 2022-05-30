def solve(n, p):
    D = [0] * (n + 1)
    if n == 1:
        return p[n]
    elif n == 2:
        return p[n - 1] + p[n]
    else:
        D[1] = p[1]
        D[2] = p[1] + p[2]
        for i in range(3, n + 1):
            D[i] = p[i] + max(D[i-2], D[i-3] + p[i-1])
        return D[n]

N = int(input())
P = [0] + [int(input()) for _ in range(N)]
answer = solve(N, P)
print(answer)