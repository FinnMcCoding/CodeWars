
def next_bigger(n):
    dig_list = []
    for digit in str(n):
        dig_list.append(int(digit))

    n = 1
    while n + 1 <= len(dig_list):
        if dig_list[-n] > dig_list[-(n+1)]:
            dig_list[-n], dig_list[-(n+1)] = dig_list[-(n+1)], dig_list[-n]
            first = dig_list[:-n]
            second = dig_list[-n:]
            for val in second.copy():
                if val < first[-1] and val > dig_list[-n]:

                    second.append(first.pop(-1))
                    first.append(val)
                    second.remove(val)
            second.sort()
            first = list(map(str, first))
            second = list(map(str,second))
            return int(''.join([*first, *second]))

        n+=1

    return -1


print(next_bigger(2864))