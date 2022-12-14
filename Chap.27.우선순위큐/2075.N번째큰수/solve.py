from heapq import heappush, heappop

import sys
input = sys.stdin.readline

heap = []

n = int(input())
for _ in range(n):
    for m in map(int, input().split()):
        heappush(heap, m)
        if len(heap) > n: heappop(heap)
print(min(heap))

