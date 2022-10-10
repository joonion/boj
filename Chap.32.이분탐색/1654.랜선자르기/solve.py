def count(L, mid):
    cnt = 0
    for i in range(len(L)):
        cnt += L[i] // mid
    return cnt

def solve(L, N):
    low, high = 1, max(L)
    while low <= high:
        mid = (low + high) // 2
        cnt = count(L, mid)
        if cnt < N:
            high = mid - 1
        else:
            low = mid + 1
    return high

K, N = map(int, input().split())
L = [int(input()) for _ in range(K)]
print(solve(L, N))