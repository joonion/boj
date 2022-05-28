def solve(n, A):
    for i in range(n):
        for j in range(i + 1, n):
            if A[i][j] != A[j][i]:
                return False
    return True
    
N = int(input())
A = [input() for _ in range(N)]
answer = solve(N, A)
print("YES" if answer else "NO")