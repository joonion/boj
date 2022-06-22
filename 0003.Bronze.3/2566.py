A = [list(map(int, input().split())) for _ in range(9)]
L, r, c = -1, -1, -1
for i in range(9):
    for j in range(9):
        if L < A[i][j]:
            L = A[i][j]; 
            r = i
            c = j
print(L)
print(r + 1, c + 1)
            
