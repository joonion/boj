def solve(n):
    low, high = 1, N
    opt = 1
    while low < high:
        mid = (low + high) // 2
        if (mid**2 + mid) // 2 <= n:
            opt = mid
            low = mid + 1
        else:
            high = mid
    return opt
    
T = int(input())
for _ in range(T):
    N = int(input())
    print(solve(N))