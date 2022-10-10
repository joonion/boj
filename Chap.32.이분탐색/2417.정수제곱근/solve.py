def solve(N):
    low, high = 0, N
    while low <= high:
        mid = (low + high) // 2
        if mid ** 2 >= N:
            high = mid - 1
        else:
            low = mid + 1
    return low

N = int(input())
print(solve(N))
