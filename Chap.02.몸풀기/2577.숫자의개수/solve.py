A = int(input())
B = int(input())
C = int(input())
N = A * B * C
count = [0 for _ in range(10)]
while N > 0:
    count[N % 10] += 1
    N //= 10
for i in range(len(count)):
    print(count[i]) 
    