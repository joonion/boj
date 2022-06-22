A = [input() for _ in range(8)]
cnt = 0
for i in range(8):
    for j in range(8):
        if not ((i % 2) ^ (j % 2)) and A[i][j] == "F":
            cnt += 1
print(cnt)
