def solve(isbn):
    s = 0
    for i, a in enumerate(isbn):
        s += int(a) * [1, 3][i % 2]
    return s

isbn = "9780921418" + input() + input() + input()
print(f"The 1-3-sum is {solve(isbn)}")