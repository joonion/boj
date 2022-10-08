def solve(n, m):
    cnt = 0
    for i in range(n, m + 1):
        cnt += str(i).count("0")
    return cnt

for _ in range(int(input())):
    N, M = map(int, input().split())
    print(solve(N, M))