def postorder(low, high, A):
    if low > high:
        return
    elif low == high:
        print(A[low])
    else:
        mid = low + 1
        while mid <= high and A[low] >= A[mid]:
            mid += 1
        postorder(low + 1, mid - 1, A)
        postorder(mid, high, A)
        print(A[low])

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readlines
A = []
for i in input():
    A.append(int(i.strip()))
postorder(0, len(A) - 1, A)