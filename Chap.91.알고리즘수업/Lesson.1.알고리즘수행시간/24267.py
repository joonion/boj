"""
$\displaystyle\sum_{k=1}^{n-2}{\sum_{x=1}^{k}{x}}$
"""
n = int(input())
print(n * (n - 1) * (n - 2) // 6)
print(3)