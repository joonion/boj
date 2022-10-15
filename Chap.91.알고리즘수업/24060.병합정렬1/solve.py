def merge(A, low, mid, high):
    global cnt, K
    B = [0] * (high - low + 1)
    i, j, k = low, mid + 1, 0
    while i <= mid and j <= high:
        if A[i] < A[j]:
            B[k], i, k = A[i], i + 1, k + 1
        else:
            B[k], j, k = A[j], j + 1, k + 1
    while i <= mid:
        B[k], i, k = A[i], i + 1, k + 1
    while j <= high:
        B[k], j, k = A[j], j + 1, k + 1
    for t in range(len(B)):
        A[low + t] = B[t]
        cnt += 1
        if cnt == K: print(B[t])
            
def mergesort(A, low, high):
    if low < high:
        mid = (low + high) // 2
        mergesort(A, low, mid)
        mergesort(A, mid + 1, high)
        merge(A, low, mid, high)

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
mergesort(A, 0, N-1)
