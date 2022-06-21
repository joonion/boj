from heapq import heappush, heappop

def solve(n, k):
    V = [0] * 100001
    PQ = []
    heappush(PQ, (abs(k - n), (n, 0)))
    V[n] = 1
    while len(PQ) > 0:
        x, d = heappop(PQ)[1]
        if x == k:
            return d
        nx = [x + 1, x - 1, 2 * x]
        for i in range(3):
            if 0 <= nx[i] <= 100000:
                heappush(PQ, (abs(k - nx[i]), (nx[i], d + 1))); 
                V[nx[i]] = 1
    
n, k = map(int, input().split())
print(solve(n, k))
