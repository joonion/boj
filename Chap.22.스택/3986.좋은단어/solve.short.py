c=0
for s in[*open(0)][1:]:
 b=[]
 for w in s.strip():b.pop()if b and w==b[-1]else b.append(w)
 c+=not b
print(c)