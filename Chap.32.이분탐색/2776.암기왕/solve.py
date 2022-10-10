def binsearch(S, x):
    low, high = 0, len(S) - 1
    while low <= high:
        mid = (low + high) // 2
        if x == S[mid]:
            return mid
        elif x < S[mid]:
            high = mid - 1
        else: # x > S[mid]
            low = mid + 1
    return -1

T = int(input())
for _ in range(T):
    N = int(input())
    A = sorted(list(map(int, input().split())))
    M = int(input())
    B = list(map(int, input().split()))
    for i in range(M):
        j = binsearch(A, B[i])
        print(0 if j < 0 else 1)