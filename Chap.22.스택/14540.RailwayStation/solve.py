def solve(n, A):
    stack = []
    j = 0
    for x in range(1, n + 1):
        stack.append(x)
        while stack and j < n and stack[-1] == A[j]:
            stack.pop()
            j += 1
    return j == n

while True:
    N = int(input())
    if N == 0: break
    while True:
        A = list(map(int, input().split()))
        if A[0] == 0: break
        print("Yes" if solve(N, A) else "No")
    print()
