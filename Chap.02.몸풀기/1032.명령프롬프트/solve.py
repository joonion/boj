def same(i, P, A):
    c = A[0][i]
    for j in range(1, len(A)):
        if c != A[j][i]:
            return False
    return True
        
n = int(input())
A = [list(input()) for _ in range(n)]
P = list("?" * len(A[0]))
for i in range(len(P)):
    if same(i, P, A):
        P[i] = A[0][i]
print("".join(P))