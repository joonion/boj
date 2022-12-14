from heapq import heappush, heappop
import sys
input = sys.stdin.readline

heap = []

N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if heap: print(heappop(heap)[1])
        else: print(0)
    else:
        heappush(heap, ((abs(x), x), x))
    
        
            