from itertools import permutations

def valid(nums, symbols):
    for i in range(len(symbols)):
        if symbols[i] == '<' and nums[i] >= nums[i+1]:
            return False
        elif symbols[i] == '>' and nums[i] <= nums[i+1]:
            return False
    return True

def solve(k, symbols):
    perms = permutations([i for i in range(10)], k + 1)
    solutions = []
    for perm in perms:
        nums = list(perm)
        if valid(nums, symbols):
            solutions.append("".join(map(str, nums)))
    return max(solutions), min(solutions)

k = int(input())
symbols = input().split()
answer1, answer2 = solve(k, symbols)
print(answer1)
print(answer2)