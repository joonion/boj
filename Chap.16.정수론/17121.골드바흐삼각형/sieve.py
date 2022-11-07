n = 1000000 // 2
sieve = [0, 0] + [1] * (n - 1)
for i in range(2, int(n**0.5) + 1):
    if sieve[i] == 1:
        for j in range(i * i, n + 1, i):
            sieve[j] = 0

# print("{",end="")
# for i in range(len(sieve)):
#     if sieve[i]: print(i, end=",")
# print("}")
print(sum(sieve))
    


    