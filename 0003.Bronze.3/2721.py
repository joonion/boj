T = [i for i in range(302)]
for i in range(1, len(T)):
    T[i] += T[i - 1]
W = [k * T[k + 1] for k in range(1, 301)]
for _ in range(int(input())):
    print(sum(W[:int(input())]))
