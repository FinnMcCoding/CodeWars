from functools import reduce
from operator import add

def max_tri_sum(numbers):
    numbers = list(dict.fromkeys(numbers))
    sort_num = sorted(numbers)
    return reduce(add, sort_num[-3:])

print(max_tri_sum([2,9,13,10,5,2,9,5]))