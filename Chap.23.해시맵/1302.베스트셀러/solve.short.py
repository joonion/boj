a=[*open(0)][1:]
t={b:0 for b in a}
for b in a:t[b]+=1
print(sorted(t.items(),key=lambda x:(-x[1],x[0]))[0][0].strip())