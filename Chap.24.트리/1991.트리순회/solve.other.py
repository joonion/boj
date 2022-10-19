import sys
input = sys.stdin.readline

def preorder(v, T):
    if v != '.':
        print(v, end="")
        preorder(T[v][0], T)
        preorder(T[v][1], T)

def inorder(v, T):
    if v != '.':
        inorder(T[v][0], T)
        print(v, end="")
        inorder(T[v][1], T)

def postorder(v, T):
    if v != '.':
        postorder(T[v][0], T)
        postorder(T[v][1], T)
        print(v, end="")

def solve(T):
    preorder('A', T)
    print()
    inorder('A', T)
    print()
    postorder('A', T)

N = int(input())
T = {}
for _ in range(N):
    r, p, q = input().split()
    T[r] = (p, q)
solve(T)

