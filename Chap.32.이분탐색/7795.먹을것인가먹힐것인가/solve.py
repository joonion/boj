def binsearch(x, B):
    low, high = 0, len(B) - 1
    while low <= high:
        mid = (low + high) // 2
        if x > B[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return low
    
def solve(A, B):
    cnt = 0
    for i in range(len(A)):
        j = binsearch(A[i], B)
        cnt += j
    return cnt

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(solve(A, sorted(B)))