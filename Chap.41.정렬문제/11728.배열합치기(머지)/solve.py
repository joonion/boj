import sys
input = sys.stdin.readline

def merge(U, V):
    T = [0] * (len(U) + len(V))
    i, j, k = 0, 0, 0
    while i < len(U) and j < len(V):
        if U[i] < V[j]:
            T[k], i, k = U[i], i+1, k+1
        else:
            T[k], j, k = V[j], j+1, k+1
    while i < len(U):
        T[k], i, k = U[i], i+1, k+1
    while j < len(V):
        T[k], j, k = V[j], j+1, k+1
    return T

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(" ".join(map(str, merge(A, B))))