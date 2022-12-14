import sys
input = sys.stdin.readline

from heapq import heappush, heappop

def solve(n, A):
    maxheap, minheap = [], []
    for a in A:
        if len(maxheap) == len(minheap):
            heappush(maxheap, -a)
        else:
            heappush(minheap, a)
        if minheap and maxheap and -maxheap[0] > minheap[0]:
            heappush(minheap, -heappop(maxheap))
            heappush(maxheap, -heappop(minheap))
        print(-maxheap[0])

N = int(input())
A = [int(input()) for _ in range(N)]
solve(N, A)