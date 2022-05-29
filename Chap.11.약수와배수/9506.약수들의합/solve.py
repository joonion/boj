from math import floor, sqrt

def divisors(n):
    divs = []
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            divs.append(i)
            if i * i != n:
                divs.append(n // i)
    return sorted(divs)    

def solve(n):
    divs = divisors(n)
    if sum(divs) + 1 != n:
        print(f"{n} is NOT perfect.")
    else:
        print(f"{n} = 1", end="")
        for i in range(len(divs)):
            print(f" + {divs[i]}", end = "")
        print()

while True:
    n = int(input())
    if n < 0:
        break
    solve(n)
