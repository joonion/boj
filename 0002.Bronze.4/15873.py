s = input()
if len(s) == 2:
    print(sum(map(int, list(s))))
elif s[:2] == "10":
    print(10 + int(s[2:]))
else:
    print(int(s[0]) + int(s[1:]))
    