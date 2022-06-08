def solve(ilow, ihigh, plow, phigh, I, P):
    # print(I[ilow:ihigh+1], P[plow:phigh+1])
    if ilow > ihigh:
        return
    elif ilow == ihigh:
        print(I[ilow], end = " ")
    else:
        mid = I.index(P[phigh])
        size = mid - ilow
        print(I[mid], end = " ")
        solve(ilow, mid-1, plow, plow+size-1, I, P)
        solve(mid+1, ihigh, plow+size, phigh-1, I, P)
    
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
I = list(map(int, input().split()))
P = list(map(int, input().split()))
solve(0, n - 1, 0, n - 1, I, P)
