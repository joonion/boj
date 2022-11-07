sieve = [i for i in range(1, 10**6, 2)]
i = 1
while i < len(sieve):
    k = sieve[i]
    j = k - 1
    while j < len(sieve):
        sieve.pop(j)
        j += k - 1
    i += 1

for i in range(len(sieve)):
    print(sieve[i])
