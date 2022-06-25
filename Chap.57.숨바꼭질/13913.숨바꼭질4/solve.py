def dfs(n, k):
    if n >= k:
        return n - k, [i for i in range(n, k - 1, -1)]
    elif k == 1: # n == 0
        return 1, [0, 1]
    elif k % 2 == 0: # k is even
        opt, path = dfs(n, k // 2)
        if k - n <= 1 + opt:
            return k - n, [i for i in range(n, k + 1)]
        else:
            return 1 + opt, path + [k]
    else: # k is odd
        opt1, path1 = dfs(n, k + 1)
        opt2, path2 = dfs(n, k - 1)
        if opt1 <= opt2:
            return 1 + opt1, path1 + [k]
        else:
            return 1 + opt2, path2 + [k]

n, k = map(int, input().split())
opt, path = dfs(n, k)
print(opt)
print(" ".join(map(str, path)))
