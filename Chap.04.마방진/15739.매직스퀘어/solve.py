def check_distinct(n, A):
    S = set([])
    for i in range(n):
        S = S.union(set(A[i]))
    return n ** 2 == len(S)
    
def check_rows(n, A, magic):
    for i in range(n):
        if sum(A[i]) != magic:
            return False
    return True

def check_cols(n, A, magic):
    for j in range(n):
        S = 0
        for i in range(n):
            S += A[i][j]
        if S != magic:
            return False
    return True

def check_lower_diag(n, A, magic):
    S = 0
    for i in range(n):
        S += A[i][i]
    return S == magic

def check_upper_diag(n, A, magic):
    S = 0
    for i in range(n):
        S += A[n - 1 - i][i]
    return S == magic

def solve(n, A):
    magic = n * (n ** 2 + 1) // 2
    if not check_distinct(n, A):
        return False
    if not check_rows(n, A, magic):
        return False
    if not check_cols(n, A, magic):
        return False
    if not check_lower_diag(n, A, magic):
        return False
    if not check_upper_diag(n, A, magic):
        return False
    return True
        
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
answer = solve(N, A)
print("TRUE" if answer else "FALSE")
