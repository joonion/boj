def charge(p, q, A):
    s = 0
    for i in range(len(A)):
        s += (A[i] // p + 1) * q
    return s
    
n = int(input())
A = list(map(int, input().split()))
y = charge(30, 10, A)
m = charge(60, 15, A)
if y == m:
    print("Y M", y)
elif y < m:
    print("Y", y)
else:
    print("M", m)
