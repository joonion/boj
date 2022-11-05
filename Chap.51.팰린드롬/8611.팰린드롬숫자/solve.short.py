n=int(input());t=1
for i in range(2,11):
 m=n;s=""
 while m:s+=str(m%i);m//=i
 if s==s[::-1]:print(i,s);t=0
if t:print("NIE")