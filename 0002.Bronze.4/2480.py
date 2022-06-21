a = list(map(int, input().split()))
b = set(a)
if len(b) == 1:
    print(10000 + a[0] * 1000)
elif len(b) == 3:
    print(max(a) * 100)
else:
    if a[0] == a[1] or a[0] == a[2]:
        print(1000 + a[0] * 100)
    else:
        print(1000 + a[1] * 100)
