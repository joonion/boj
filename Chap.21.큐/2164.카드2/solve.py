def solve(n):
    queue = [i for i in range(1, n + 1)]
    while len(queue) > 1:
        queue.pop(0)
        queue.append(queue.pop(0))
    return queue[0]

N = int(input())
print(solve(N))
