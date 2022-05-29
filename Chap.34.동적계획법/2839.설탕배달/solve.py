def solve(n):
    global INF
    smallest = INF
    for i in range(n // 5 + 1):
        for j in range(n // 3 + 1):
            if i*5 + j*3 == n:
                smallest = min(smallest, i + j)
                # print(smallest, i, j)
    return -1 if smallest == INF else smallest

INF = 5000
N = int(input())
answer = solve(N)
print(answer)
