def solve(n, A):
    H = {}
    for s in A:
        for i in range(len(s)):
            H[s[i]] = H[s[i]] + 10 ** i if s[i] in H else 10 ** i
    head = set()
    if len(H) == 10:
        for i in range(len(A)):
            head.add(A[i][-1])
        small = 10 ** 12
        for h in set(H.keys()) - head:
            if H[h] < small:
                small = H[h]
                key = h
        H[key] = 0
    V = sorted(H.values(), reverse = True)
    S = 0
    for i in range(len(H)):
        S += (9 - i) * V[i]
    return S

n = int(input())
A = [input()[::-1] for _ in range(n)]
print(solve(n, A))