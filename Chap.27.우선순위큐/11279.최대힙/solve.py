import sys
input = sys.stdin.readline
print = sys.stdout.write

from heapq import heappush, heappop

def solve(n):
    heap = []
    for _ in range(n):
        x = int(input())
        if x == 0:
            print("0" if len(heap) == 0 else str(-heappop(heap)))
            print("\n")
        else:
            heappush(heap, -x)

n = int(input())
solve(n)
