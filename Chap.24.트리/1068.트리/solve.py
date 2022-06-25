def leaf(node, d, T):
    if len(T[node]) == 0:
        return 1
    else:
        cnt = 0
        for i in range(len(T[node])):
            cnt += leaf(T[node][i], d, T)
        return cnt

n = int(input())
A = list(map(int, input().split()))
d = int(input())
T = [[] for _ in range(n)]
for i in range(n):
    if A[i] >= 0 and i != d:
        T[A[i]].append(i)
root = A.index(-1)
print(0 if root == d else leaf(root, d, T))