def solve(n, k):
    queue = [i for i in range(1, n + 1)]
    seq = []
    target = 0
    while len(queue) > 0:
        target = (target + k - 1) % len(queue)
        seq.append(queue.pop(target))
    return seq

N, K = map(int, input().split())
answer = solve(N, K)
print("<", end = "")
for i in range(len(answer)):
    if i < N - 1:
        print(f"{answer[i]}, ", end = "")
    else:
        print(f"{answer[i]}>")