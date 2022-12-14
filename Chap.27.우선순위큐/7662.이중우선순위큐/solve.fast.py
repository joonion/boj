import sys
input = sys.stdin.readline
from heapq import heappush, heappop

for _ in range(int(input())):
    k = int(input())
    maxheap = []
    minheap = []
    for i in range(k):
        cmd, item = input().split()
        n = int(item)
        if cmd == 'I':
            heappush(maxheap, (-n, n))
            heappush(minheap, (n, n))
        elif maxheap:
            if n == 1:
                x = heappop(maxheap)[1]
                minheap.remove((x, x))
            else:
                x = heappop(minheap)[1]
                maxheap.remove((-x, x))
    if maxheap:
        print(maxheap[0][1], minheap[0][1])
    else:
        print("EMPTY")