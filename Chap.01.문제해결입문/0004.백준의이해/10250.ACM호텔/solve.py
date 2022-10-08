def solve(H, W, n):
    h = (n - 1) % H + 1
    w = (n - 1) // H + 1
    return h, w

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    h, w = solve(H, W, N)
    print(f"{h}{w:02d}")
    