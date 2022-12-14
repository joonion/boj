def dfs(i, n, s):
    if i == n:
        print(s)
    else:
        for i in range(N):
            j = s.pop(i)
            s.sort()
            dfs(i + 1, n, j + s)
            s.insert(i, j)

N = int(input())
S = list(range(1, N + 1))
dfs(0, N, S)