def knapsack(n, W, w, p, DP):
    if n == 0 or W <= 0:
        DP[(n, W)] = 0
    else:
        if (n, W) not in DP:
            if w[n] > W:
                DP[n, W] = knapsack(n-1, W, w, p, DP)
            else:
                DP[n, W] = max(knapsack(n-1, W-w[n], w, p, DP) + p[n],
                               knapsack(n-1, W, w, p, DP))
    return DP[(n, W)]

n, W = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(n)]
A.sort(reverse = True, key = lambda x: x[1]/x[0])
w, p = [0] * (n + 1), [0] * (n + 1)
for i in range(1, n + 1):
    w[i], p[i] = A[i-1][0], A[i-1][1]
print(knapsack(n, W, w, p, {}))
