while True:
    N = int(input())
    if N == 0: break
    T = {}
    for _ in range(N):
        s = input()
        t = "".join(sorted(s))
        if t in T:
            T[t][0] += 1
        else:
            T[t] = [0, s]
    maxval = max(T.values(), key = lambda x: x[0])
    print(maxval[1], maxval[0])
