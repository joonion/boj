a,b,c=input(),input(),[0]*26
for d in a:c[ord(d)-97]+=1
for d in b:c[ord(d)-97]-=1
print(sum(map(abs,d)))