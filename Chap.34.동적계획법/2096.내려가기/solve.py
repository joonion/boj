import sys
input = sys.stdin.readline
n = int(input())
M, m = [0] * 3, [0] * 3
T, t = [0] * 3, [0] * 3
for _ in range(n):
    a, b, c = list(map(int, input().split()))
    T[0] = a + max(M[0], M[1])
    T[1] = b + max(M)
    T[2] = c + max(M[1], M[2])
    t[0] = a + min(M[0], M[1])
    t[1] = b + min(M)
    t[2] = c + min(M[1], M[2])
    for i in range(3):
        M[i], m[i] = T[i], t[i]
print(max(M), min(m))    
