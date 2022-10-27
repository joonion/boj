def solve(n, k, A):
    cnt = 0
    for last in range(n - 1, 0, -1):
        i = A.index(max(A[:last+1]))
        if last != i:
            A[last], A[i] = A[i], A[last]
            cnt += 1
            if cnt == k:
                print(A[i], A[last])
                return
    print(-1)

N, K = map(int, input().split())
A = list(map(int, input().split()))
solve(N, K, A)