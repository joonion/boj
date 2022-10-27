W={}
while 1:
 try:
  w2="".join(sorted(w1:=input()))
  W.setdefault(w2,[]).append(w1)
 except EOFError:break
for k in W:W[k].sort()
S=sorted(W.values(),key=lambda x:(-len(x),x[0]))
for s in S[:5]:print(f"Group of size {len(s)}: {' '.join(sorted(set(s)))} .")
