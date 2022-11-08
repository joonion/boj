t = int(input())
for _ in range(t):
    k = int(input())
    s = ""
    while k > 0:
        s += chr(ord('A') + (k - 1) % 26)
        k = (k - 1) // 26
    print(s[::-1])
        