def partition(p, r, A):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    i += 1
    if i != r:
        A[i], A[j] = A[j], A[i]
    return i
            
def select(p, r, q, k, A):
    if p == r:
        return A[p]
    t = partition(p, r, A)
    k = t - p + 1
    if q == k:
        return A[t]
    elif q < k:
        select(p, t - 1, q, k, A)
    else:
        select(t + 1, r, q - k, A)

def solve(n, q, k, A):
    select(0, n - 1, q, k, A)
    
N, Q, K = map(int, input().split())
A = list(map(int, input().split()))
solve(N, Q, K, A)