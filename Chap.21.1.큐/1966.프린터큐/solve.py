def largest(p, q):
    for i in range(len(q)):
        if p < q[i][1]:
            return False
    return True

def solve(N, M, P):
    queue = [(i, P[i]) for i in range(N)]
    cnt = 0
    while True:
        cur = queue.pop(0)
        if not largest(cur[1], queue):
            queue.append(cur)
        else:
            cnt += 1 # Increase print count
            if cur[0] == M:
                break
    return cnt

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    print(solve(N, M, P))
    