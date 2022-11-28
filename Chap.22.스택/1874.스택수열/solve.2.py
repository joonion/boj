# 출력 수열을 먼저 처리

def solve(n, A):
    stack = []
    j = 1
    for i in A:
        while j <= i:
            stack.append(j)
            j += 1
            op += "+"
        if stack[-1] == i:
            stack.pop(0)
            op += "-"
        else:
            op = "No"
            break
    print("\n".join(op))


import sys
input = sys.stdin.readline
n = int(input())
A = [int(input()) for _ in range(n)]
solve(n, A)
