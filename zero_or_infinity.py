
from decimal import *
def going(n):
    sum = 0
    i =0
    previous_sum = -1
    stop = False
    previous = 1
    while not stop and i < n-1:
        sum += 1/(previous*(n-i))
        test_sum = round(sum, 6)
        previous = (previous*(n-i))
        print(sum)
        if test_sum == previous_sum:
            stop = True
        else:
            previous_sum = test_sum
            i += 1
    context = Context(prec=7,rounding=ROUND_DOWN)
    g = context.create_decimal_from_float(sum+1)
    a = float(round(Decimal(sum + 1),6))
    if n <8:
        return a
    else:
        return float(g)

print(going(5))