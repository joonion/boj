from math import floor, ceil, sqrt
def solve(m, n):
    perfect = []
    for i in range(ceil(sqrt(m)), floor(sqrt(n)) + 1):
        perfect.append(i ** 2)
    if len(perfect) == 0:
        return -1, None
    return sum(perfect), perfect[0]

M = int(input())
N = int(input())
answer1, answer2 = solve(M, N)
print(answer1)
if answer1 > 0:
    print(answer2)