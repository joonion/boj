import sys
input = sys.stdin.readline

from heapq import heappush, heappop

def solve(k, A):
    maxheap, minheap = [], []
    for cmd, item in A:
        i = int(item)
        if cmd == 'I':
            heappush(maxheap, (-i, i))
            heappush(minheap, (i, i))
        elif maxheap:
            if i == 1:
                x = heappop(maxheap)[1]
                minheap.remove((x, x))
            else:
                x = heappop(minheap)[1]
                maxheap.remove((-x, x))
    if maxheap:
        print(heappop(maxheap)[1], heappop(minheap)[1])
    else:
        print("EMPTY")
        
for _ in range(int(input())):
    k = int(input())
    A = [input().split() for _ in range(k)]
    solve(k, A)