import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    n = int(input())
    print(n, "lucky" if solve(n) else "unlucky")