def solve(divs):
    divs.sort()
    return divs[0] * divs[-1]

N = int(input())
divs = list(map(int, input().split()))
answer = solve(divs)
print(answer)