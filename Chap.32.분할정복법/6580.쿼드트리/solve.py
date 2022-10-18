def check(i, j, n, A):
    chk = A[i][j]
    for r in range(i, i + n):
        for c in range(j, j + n):
            if A[r][c] != chk: 
                return 2
    return chk

def quadtree(i, j, n, A):
    if n == 1:
        return "W" if A[i][j] == 0 else "B"
    else:
        chk = check(i, j, n, A)
        if chk < 2:
            return "W" if chk == 0 else "B"
        else:
            m = n // 2
            s1 = quadtree(i, j, m, A)
            s2 = quadtree(i, j+m, m, A)
            s3 = quadtree(i+m, j, m, A)
            s4 = quadtree(i+m, j+m, m, A)
            return "Q" + s1 + s2 + s3 + s4
        
def solve(n, A):
    return quadtree(0, 0, n, A)
        
def tolist(n, a):
    x = 0
    for i in range(n // 8):
        t = int(a[i], 16)
        t = int("{0:08b}".format(t)[::-1], 2)
        x = (x << 8) + t
    y = list(map(int, bin(x)[2:]))
    return [0] * (n - len(y)) + y 

N = int(input().split()[2])
input()
input()
A = []
for i in range(N):
    a = input().split(",")
    A.append(tolist(N, a))
for i in range(N):
    print("".join(map(str, A[i])))
input()

print(N)
print(solve(N, A))