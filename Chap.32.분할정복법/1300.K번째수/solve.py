def count(N, mid):
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(mid // i, N)
    return cnt

def solve(N, k):
    low, high = 1, k
    while low < high:
        mid = (low + high) // 2
        if k <= count(N, mid):
            high = mid
        else:
            low = mid + 1
    return low

N = int(input())
k = int(input())
answer = solve(N, k)
print(answer)

