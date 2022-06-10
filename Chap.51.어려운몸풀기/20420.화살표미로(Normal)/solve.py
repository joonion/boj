from heapq import heappush, heappop
import sys
input = sys.stdin.readline

D = "URDL"
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def bfs(n, m, k, A):

n, m, k = map(int, input().split())
A = [input().strip() for _ in range(n)]
print("Yes" if bfs(n, m, k, A) else "No")