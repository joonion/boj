n = int(input())
c = 0
for i in range((n+1)//3, (n+1)//2): c += (3*i-n+2)//2
print(c)