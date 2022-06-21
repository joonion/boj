a,b,c,d,e = [int(input()) for _ in range(5)]
print(min(a+d-50, a+e-50, b+d-50, b+e-50, c+d-50, c+e-50))