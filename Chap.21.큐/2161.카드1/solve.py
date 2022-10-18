def solve(n):
    queue, sequence = [i for i in range(1, n + 1)], []
    while len(queue) > 1:
        sequence.append(queue.pop(0))
        queue.append(queue.pop(0))
    sequence.append(queue.pop(0))
    return sequence

N = int(input())
S = solve(N)
print(" ".join(map(str, S)))
