import decimal
from decimal import Decimal, ROUND_DOWN
decimal.getcontext().prec = 1000

T = int(input())
for _ in range(T):
    N = Decimal(input() + '.0000000000')
    D = round(Decimal(N ** (Decimal("1") / Decimal("3"))), 500)
    d = Decimal(D).quantize(Decimal('.0000000001'), rounding = ROUND_DOWN)
    print(f"{d:.11f}"[:-1])    