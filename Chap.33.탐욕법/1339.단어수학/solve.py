from heapq import heappush, heappop

def solve(n, A):
    H = {}
    for s in A:
        for i in range(len(s)):
            H[s[i]] = H[s[i]] + 10 ** i if s[i] in H else 10 ** i
    V = sorted(H.values(), reverse = True)
    S = 0
    for i in range(len(H)):
        S += (9 - i) * V[i]
    return S

n = int(input())
A = [input()[::-1] for _ in range(n)]
print(solve(n, A))
