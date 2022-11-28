INF = 10 ** 6

def solve(n):
    if n in [2, 5]:
        return 1
    elif n == 4:
        return 2
    elif n < 5:
        return -1
    else:
        T = [INF] * (n + 1)
        T[2] = T[5] = 1
        T[4] = 2
        for i in range(6, n + 1):
            T[i] = 1 + min(T[i - 2], T[i - 5])
        return T[n] if T[n] < INF else -1
    
N = int(input())
print(solve(N))