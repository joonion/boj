def solve(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return solve(n - 1, k - 1) + solve(n - 1, k)
    
N, K = map(int, input().split())
answer = solve(N, K)
print(answer)