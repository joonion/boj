def binsearch(n, F):
    low, high = 0, len(F) - 1
    while low <= high:
        mid = (low + high) // 2
        if n == F[mid]:
            return mid
        elif n < F[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
            
def fib(n):
    F = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        F[i] = F[i-1] + F[i-2]
    return F

F = fib(100000)
T = int(input())
for _ in range(T):
    N = int(input())
    print(binsearch(N, F))
    
        