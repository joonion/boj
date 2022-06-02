import sys
input = sys.stdin.readline 

def sumcolor(i, j, n, M):
    S = 0
    for r in range(i, i + n):
        S += sum(M[r][j:j+n])
    return S

def cut(i, j, n, M):
    global white, blue
    if n == 1:
        if M[i][j] == 0:
            white += 1
        else:
            blue += 1
    else:
        S = sumcolor(i, j, n, M)
        if S == 0:
            white += 1
        elif S == n * n:
            blue += 1
        else:
            m = n // 2
            cut(i, j, m, M)
            cut(i, j+m, m, M)
            cut(i+m, j, m, M)
            cut(i+m, j+m, m, M)
        
def solve(n, M):
    return cut(0, 0, n, M)
    
N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0
solve(N, M)
print(white)
print(blue)