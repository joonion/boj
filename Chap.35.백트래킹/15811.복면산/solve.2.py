from itertools import permutations

def to_int(w, D):
    c = list(w[::-1])
    n = 0
    for i in range(len(c)):
        n += D[c[i]] * (10**i)
    return n

def is_valid(D, w1, w2, w3):
    n1 = to_int(w1, D)
    n2 = to_int(w2, D)
    n3 = to_int(w3, D)
    return n1 + n2 == n3

def solveto(i, n, r1, r2, r3):
    if i <= n:
        

def solve(w1, w2, w3):
    n = max(len(w1), len(w2), len(w3))
    solveto(0, n, w1[::-1], w2[::-1], w3[::-1])
    
w1, w2, w3 = input().split()
print("YES" if solve(w1, w2, w3) else "NO")
