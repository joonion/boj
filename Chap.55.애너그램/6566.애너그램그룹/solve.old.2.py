import sys
input = sys.stdin.readline
H = {}
while True:
    try:
        w1 = input().strip()
        if w1 == "": break
        w2 = "".join(sorted(list(w1)))
        if w2 not in H:
            H[w2] = [w1]
        else:
            H[w2].append(w1)
    except EOFError:
        break
for key in H:
    H[key].sort()
S = sorted(H.items(), key=lambda x: (-len(x[1]), x[1]))
for i in range(len(S)):
    if i == 5: break
    print(f"Group of size {len(S[i][1])}:", " ".join(S[i][1]), ".")
    
        