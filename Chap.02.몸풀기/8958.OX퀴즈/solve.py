T = int(input())
for _ in range(T):
    S = input().strip()
    k, score, total = S[0], 0, 0
    for i in range(0, len(S)):
        if S[i] == "X":
            score = 0
        else:
            score += 1
        total += score
    print(total)            
        
        