a=[];n=int(input())
for _ in[0]*n:a=sorted(a+[*map(int,input().split())])[-n:]
print(a[0])