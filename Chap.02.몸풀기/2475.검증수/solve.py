digits = list(map(int, input().split()))
sumofsqr = 0
for i in range(len(digits)):
    sumofsqr += digits[i] ** 2
print(sumofsqr % 10)