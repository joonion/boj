def solve(n):
    D = [0, 0, 1, 1] + [0] * (n - 3)
    P = [0, 1, 1, 1] + [0] * (n - 3)
    if n > 3:
        for i in range(4, n + 1):
            D[i], P[i] = 1 + D[i - 1], i - 1
            if i % 3 == 0 and D[i] > 1 + D[i // 3]:
                D[i], P[i] = 1 + D[i // 3], i // 3
            if i % 2 == 0 and D[i] > 1 + D[i // 2]:
                D[i], P[i] = 1 + D[i // 2], i // 2
    return D[n], P
        
n = int(input())
opt, P = solve(n)
print(opt)
print(n, end = " ")
while n > 1:
    print(P[n], end = " ")
    n = P[n]