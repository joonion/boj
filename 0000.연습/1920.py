n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

A.sort()
for i in range(m):
    t, low, high = B[i], 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] == t:
            print(1)
            break
        elif A[mid] < t:
            low = mid + 1
        else:
            high = mid - 1
    if low > high:
        print(0)
        