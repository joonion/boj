def dfs(n, k):
    if n >= k:
        return n - k
    elif k == 1: # n == 0
        return 1
    elif k % 2 == 0: # k is even
        return min(k - n, 1 + dfs(n, k // 2))
    else: # k is odd
        return 1 + min(dfs(n, k + 1), dfs(n, k - 1))
    
n, k = map(int, input().split())
print(dfs(n, k))
