while True:
    A = list(map(int, input().split()))
    A.sort()
    a, b, c = A
    if a == 0 and b == 0 and c == 0:
        break
    if a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")