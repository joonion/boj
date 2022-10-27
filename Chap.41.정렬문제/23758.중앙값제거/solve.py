from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def solve(heap):
    cnt = 0
    while True:
        cnt += 1
        m = -heap[0] // 2
        # print(m)
        if m == 0: break
        heappop(heap)
        heappush(heap, -m)
    return cnt

n = int(input())
S = list(map(int, input().split()))
heap = []
for i in range(n):
    j = S[i]
    if len(heap) <= (n - 1) // 2:
        heappush(heap, -j)
    elif j < -heap[0]:
        heappop(heap)
        heappush(heap, -j)
# print(heap)
print(solve(heap))
