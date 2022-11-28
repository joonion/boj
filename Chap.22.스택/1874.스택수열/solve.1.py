# 1부터 n까지를 먼저 처리

def solve(n, A):
    stack, op = [], []
    j = 0
    for i in range(1, n + 1):
        stack.append(i)
        op += "+"
        while stack and A[j] == stack[-1]:
            stack.pop()
            j += 1
            op += "-"
    print("NO" if len(stack) != 0 else "\n".join(op))

import sys
input = sys.stdin.readline
n = int(input())
A = [int(input()) for _ in range(n)]
solve(n, A)
