import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def solve(A):
    LPQ, RPQ = [], []
    for a in A:
        if not LPQ or a <= -LPQ[0]:
            heappush(LPQ, -a)
        else:
            heappush(RPQ, a)
        if len(LPQ) < len(RPQ):
            heappush(LPQ, -heappop(RPQ))
        elif len(LPQ) > len(RPQ) + 1:
            heappush(RPQ, -heappop(LPQ))
        print(-LPQ[0] if len(LPQ) != len(RPQ) else min(-LPQ[0], RPQ[0]))

A = [int(input()) for _ in range(int(input()))]
solve(A)
