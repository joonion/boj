import sys
input = sys.stdin.readline

for i in range(int(input())):
    a, b = input().strip(), input().strip()
    c = [0] * 26
    for d in a:
        c[ord(d) - ord('a')] += 1
    for d in b:
        c[ord(d) - ord('a')] -= 1
    print(f"Case #{i+1}: {sum(map(abs, c))}")
