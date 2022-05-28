def fill(line, magic):
    for i in range(3):
        if line[i] == 0:
            line[i] = magic - sum(line)
            
def find_magic(A):
    for i in range(3):
        if 0 not in A[i]:
            return sum(A[i])
    for j in range(3):
        col = [A[i][j] for i in range(3)]
        if 0 not in col:
            return sum(col)
    diag = [A[i][i] for i in range(3)]
    if 0 not in diag:
        return sum(diag)
    diag = [A[2 - i][i] for i in range(3)]
    if 0 not in diag:
        return sum(diag)
    S = 0
    for i in range(3):
        S += sum(A[i])
    return S // 2
                
def solve(A):
    magic = find_magic(A)
    for i in range(3):
        if sum(A[i]) != magic and A[i].count(0) == 1:
            fill(A[i], magic)
    for j in range(3):
        col = [A[i][j] for i in range(3)]
        if sum(col) != magic:
            for i in range(3):
                if A[i][j] == 0:
                    A[i][j] = magic - sum(col)
    
A = [list(map(int, input().split())) for _ in range(3)]
solve(A)
for i in range(3):
    print(" ".join(map(str, A[i])))
