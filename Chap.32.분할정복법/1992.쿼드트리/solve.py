import sys
input = sys.stdin.readline

def check(k, i, j, n, A):
    for r in range(i, i + n):
        for c in range(j, j + n):
            if A[r][c] != k: return False
    return True

def quadtree(i, j, n, A):
    if n == 1:
        return str(A[i][j])
    elif check(0, i, j, n, A):
        return "0"
    elif check(1, i, j, n, A):
        return "1"
    else:
        m = n // 2
        s1 = quadtree(i, j, m, A)
        s2 = quadtree(i, j+m, m, A)
        s3 = quadtree(i+m, j, m, A)
        s4 = quadtree(i+m, j+m, m, A)
        return "(" + s1 + s2 + s3 + s4 + ")"
    
def solve(n, A):
    return quadtree(0, 0, n, A)
    
n = int(input())
A = [list(map(int, list(input().strip()))) for _ in range(n)]    
answer = solve(n, A)
print(answer)
