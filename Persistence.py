
def persistence(num):
    i = 0
    while len(str(num)) != 1:
        number  = 1
        for value in str(num):
            number = number*int(value)

        num = number
        i += 1
    return [num, i]

print(persistence(4))
