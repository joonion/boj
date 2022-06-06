import sys
input = sys.stdin.readline

def solve(n, T):
    for i in range(len(T) - 2, -1, -1):
        for j in range(i + 1):
            T[i][j] += max(T[i + 1][j], T[i + 1][j + 1])
    return T[0][0]

n = int(input())
T = [list(map(int, input().split())) for _ in range(n)]
print(solve(n, T))