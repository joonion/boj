def update(pos, val, A):
    A[pos] = val
    
def query(l, r, A):
    return sum(A[l:r+1])
    
n, m, k = map(int, input().split())
A = [0] + [int(input()) for _ in range(n)]
for _ in range(m + k):
    c, a, b = map(int, input().split())
    if c == 1:
        update(a, b, A)
    else:
        print(query(a, b, A))