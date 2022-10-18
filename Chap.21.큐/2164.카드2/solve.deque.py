from collections import deque
n = int(input())
A = deque([i for i in range(1, n + 1)])
while len(A) > 1:
    A.popleft()
    A.rotate(-1)
print(A[0])
