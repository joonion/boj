import sys
input = sys.stdin.readline

def solve(n):
    MAX, MIN = [[0] * 3, [0] * 3], [[0] * 3, [0] * 3]
    for i in range(n):
        cur, prv = i % 2, (i - 1) % 2
        a, b, c = map(int, input().split())
        MAX[cur][0] = a + max(MAX[prv][0], MAX[prv][1])
        MAX[cur][1] = b + max(MAX[prv])
        MAX[cur][2] = c + max(MAX[prv][1], MAX[prv][2])
        MIN[cur][0] = a + min(MIN[prv][0], MIN[prv][1])
        MIN[cur][1] = b + min(MIN[prv])
        MIN[cur][2] = c + min(MIN[prv][1], MIN[prv][2])
    return max(MAX[cur]), min(MIN[cur])        

n = int(input())
ans1, ans2 = solve(n)
print(ans1, ans2)
