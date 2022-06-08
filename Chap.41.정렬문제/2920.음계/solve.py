import sys
input = sys.stdin.readline
A = list(map(int, input().split()))
B = sorted(A)
C = sorted(A, reverse = True)
if (A == B):
    print("ascending")
elif (A == C):
    print("descending")
else:
    print("mixed")