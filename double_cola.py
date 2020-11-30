# https://www.codewars.com/kata/551dd1f424b7a4cdae0001f0/train/python

def who_is_next(names, r):
    n = 0
    power = len(names) * (2**n)
    sum = 0
    while sum < r:
        sum += power
        n += 1
        power = len(names) * (2 ** n)

    if n != 1 :
            n -= 1
    elif n == 1:
        return names[r - 1]

    power = len(names) * (2 ** n)
    print(r,sum,power)
    leftover = r - (sum - power)
    num = leftover/power

    no_peeps_frac = 1/len(names)
    for value in range(1,len(names)+1):
        if no_peeps_frac*(value -1) < num and num <= no_peeps_frac*value:
            return names[value - 1]
        elif num == 0:
            return names[-1]



print(who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 10))