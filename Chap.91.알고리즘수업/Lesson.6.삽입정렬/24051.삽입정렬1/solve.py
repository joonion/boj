def solve(n, k, A):
    cnt = 0
    for i in range(1, n):
        t = A[i]
        j = i - 1
        while j >= 0 and A[j] > t:
            A[j + 1] = A[j]
            j -= 1
            cnt += 1
            if cnt == k:
                print(A[j + 1])
                return
        if j + 1 != i:
            A[j + 1] = t
            cnt += 1
            if cnt == k:
                print(A[j + 1])
                return
    print(-1)

N, K = map(int, input().split())
A = list(map(int, input().split()))
solve(N, K, A)