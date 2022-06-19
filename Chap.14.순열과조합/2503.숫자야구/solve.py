from itertools import permutations

def check(n, A):
    for i in range(len(A)):
        m = list(map(int, list(str(A[i][0]))))
        s, b = 0, 0
        for j in range(3):
            if n[j] == m[j]:
                s += 1
            elif n[j] in m:
                b += 1
        if s != A[i][1] or b != A[i][2]:
            return False
    return True
        
def solve(A):
    cnt = 0
    perm = permutations([i for i in range(1, 10)], 3)
    for p in perm:
        n = list(p)
        if check(n, A):
            cnt += 1
    return cnt
        
A = [list(map(int, input().split())) for _ in range(int(input()))]
print(solve(A))
