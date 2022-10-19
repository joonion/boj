def solve(n, m):
    T = {}
    for i in range(m - 1):
        T[i] = m - 1
    for i in range(m - 1, n - 1):
        T[i] = i + 1
    return T
    
n, m = map(int, input().split())
T = solve(n, m)
for key in T:
    print(key, T[key])