w,s=[0]*99,0
for i in[1]*int(input()):
 for c in input()[::-1]:w[ord(c)]-=i;i*=10
w.sort()
for i in range(10):s+=w[i]*(i-9)
print(s)