def solve(n, k):
    if n == 1:
        return 0
    else:
        return solve(n - 1, )
    
N, K = map(int, input())
solve(N, K)