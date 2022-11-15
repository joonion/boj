def solve(n):
    low, high = 0, n
    while high <= low:
        mid = (low + high) // 2
        if mid ** 3 > n:
            high = mid - 1
        else:
            low = mid + 1
    return high
    
for _ in range(int(input())):
    m = solve(int(input()) * (10 ** 30))
    print(f"{m // 10**30}.{m % 10 ** 30:010d}")
