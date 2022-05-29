def solve(books):
    cntmap = {}
    for book in books:
        cntmap[book] = cntmap[book] + 1 if book in cntmap else 1
    bestcnt = max(cntmap.values())
    bestsellers = []
    for book in cntmap.keys():
        if cntmap[book] == bestcnt:
            bestsellers.append(book)
    bestsellers.sort()
    return bestsellers[0]

N = int(input())
books = []
for _ in range(N):
    books.append(input())
answer = solve(books)
print(answer)
        