def solve(n):
    D = [0] * (n + 1)
    if n < 2:
        return 0
    if n == 2 or n == 3:
        return 1
    else:
        D[2] = D[3] = 1
        for i in range(4, n + 1):
            D[i] = D[i - 1] + 1
            if i % 3 == 0:
                D[i] = min(D[i], D[i // 3] + 1)
            if i % 2 == 0:
                D[i] = min(D[i], D[i // 2] + 1)
    return D[n]            
    
N = int(input())
answer = solve(N)
print(answer)