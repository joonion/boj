def solve(n, A):
    stack = []
    for i in range(n):
        while len(stack) != 0 and stack[-1] <= A[i]:
            if (len(stack) > 0):            
                stack.pop()
        stack.append(A[i])
    return len(stack)

import sys
input = sys.stdin.readline
N = int(input())
A = [int(input()) for _ in range(N)]
print(solve(N, A))