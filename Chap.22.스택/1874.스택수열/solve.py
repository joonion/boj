n = int(input())
A = [int(input()) for _ in range(n)]
queue = [i for i in range(1, n + 1)]
stack = []
while queue:
    t = queue.pop(0)
    if t <= A[0]: 
        stack.append(t)
    else:
        while True:
            if not stack:
                break
            if stack.pop() == A[0]:
                break
        A.pop(0)
    print(A, queue, stack)            
            
        