def solve(n, A):
    stack = [A[0]]
    for i in range(1, n):
        if stack[-1] < A[i]:
            stack.append(A[i])
    return len(stack), stack
        
N = int(input())
A = list(map(int, input().split()))
L, S = solve(N, A)
print(L)
print(" ".join(map(str, S)))
