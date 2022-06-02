x = [sum(map(int,s.split('+'))) for s in input().split('-')]
print(x[0] - sum(x[1:]))