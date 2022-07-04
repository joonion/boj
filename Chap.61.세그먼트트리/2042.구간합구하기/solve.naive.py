def update(pos, val, A):
    A[pos] = val
    
def sumofrange(l, r, A):
    return sum(A[l:r+1])
    
n, m, k = map(int, input().split())
A = [0] + [int(input()) for _ in range(n)]
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c, A)
    elif a == 2:
        print(sumofrange(b, c, A))