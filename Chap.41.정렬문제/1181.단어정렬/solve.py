import sys
input = sys.stdin.readline
n = int(input())
A = [input().strip() for _ in range(n)]
A = list(set(A))
A.sort(key = lambda x : (len(x), x))
print("\n".join(A))