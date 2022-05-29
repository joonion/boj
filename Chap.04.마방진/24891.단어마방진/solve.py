def promising(i, m, D, S):
    if len(S) == 0:
        return True
    else:
        target, word = D[S[0]], D[i]
        return word[0] == target[len(S)]

def check(D, S):
    T = [D[s] for s in S]
    for i in range(1, len(T)):
        for j in range(i + 1, len(T[0])):
            if T[i][j] != T[j][i]:
                return False
    return True
    
def search(m, n, D, S):
    if m == 0:
        return None if not check(D, S) else [D[s] for s in S]
    else:
        for i in range(n):
            if i not in S and promising(i, m, D, S):
                S.append(i)
                solution = search(m - 1, n, D, S) 
                if solution != None:
                    return solution
                S.pop()
        return None

def solve(m, n, D):
    D.sort()
    solution = search(m, n, D, [])
    if solution == None:
        print("NONE")
    else:
        for i in range(m):
            print(solution[i])

import sys
input = sys.stdin.readline
L, N = map(int, input().strip().split())
D = [input().strip() for _ in range(N)]
solve(L, N, D)
