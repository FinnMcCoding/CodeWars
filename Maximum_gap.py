import numpy as np

def max_gap(numbers):
    sort_num = sorted(numbers)
    sums = list(np.diff(sort_num))
    return max(sums)


print(max_gap([13,10,2,9,5]))



