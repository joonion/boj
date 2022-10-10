def count(B, length):
    cnt = 0
    for i in range(len(B)):
        cnt += B[i] // length
    return cnt
    
def solve(B, N):
    low, high = 1, max(B)
    while low <= high:
        mid = (low + high) // 2
        score = count(B, mid)
        if score < N:
            high = mid - 1
        else:
            low = mid + 1
    return high

N, M = map(int, input().split())
B = [int(input()) for _ in range(M)]
print(solve(B, N))