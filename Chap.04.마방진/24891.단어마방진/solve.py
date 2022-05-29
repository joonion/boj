

def promising(D, S):
    if len(S) == 0:
        return True
    else:
        return True

def search(m, n, D, S, solution):
    if m == 0 and promising(D, S):
        candidate = "".join([D[s] for s in S])
        solution[0] = min(solution[0], candidate)
    else:
        for i in range(n):
            if i not in S and promising(D, S):
                S.append(i)
                search(m - 1, n, D, S, solution) 
                S.pop()
            
def solve(m, n, D):
    solution = ["Z" * (m * m)]
    search(m, n, D, [], solution)
    if solution[0] == "Z" * (m * m):
        print("NONE")
    else:
        for i in range(m):
            print(solution[0][i*m : i*m + m])
    
L, N = map(int, input().split())
D = [input() for _ in range(N)]
solve(L, N, D)
