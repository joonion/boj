n = int(open(0).read())
c = 0
for a in range((n+1)//3, (n+1)//2):
    c += (3*a-n+2)//2
print(c)