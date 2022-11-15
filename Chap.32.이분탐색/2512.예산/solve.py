def budget(n, s, upper):
    total = 0
    for i in range(n):
        total += s[i] if s[i] < upper else upper
    return total

def solve(n, m, s):
    low, high = 0, max(s)
    while low <= high:
        mid = (low + high) // 2
        if budget(n, s, mid) <= m:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1
    
N = int(input())
S = list(map(int, input().split()))
M = int(input())
print(solve(N, M, S))