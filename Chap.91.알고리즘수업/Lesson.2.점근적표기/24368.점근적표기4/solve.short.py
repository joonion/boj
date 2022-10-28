def solve():
  a, b, c, d, n0 = map(int, open(0).read().split())
  if a > d: return 0
  for x in range(n0, int(1e6)):
    if a*x*x+b*x+c > d*x*x:
      return 0
  if a == d:
    return 1
  x0 = -b / (2 * (a-d))
  if x0 >= n0 and a*x0*x0+b*x0+c > d*x0*x0:
    return 0
  return 1

print(solve())