def cut(H, height):
    length = 0
    for i in range(len(H)):
        length += (H[i] - height) if H[i] > height else 0
    return length
        
def solve(H, M):
    low, high = 0, max(H)
    while low <= high:
        mid = (low + high) // 2
        length = cut(H, mid)
        # print(low, high, mid, length)
        if length < M:
            high = mid - 1
        else:
            low = mid + 1
    return high

N, M = map(int, input().split())
H = list(map(int, input().split()))
print(solve(H, M))
