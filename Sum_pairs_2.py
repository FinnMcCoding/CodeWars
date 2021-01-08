

def sum_pairs(ints,s):
    x = 1
    ints = f7(ints)
    print(ints)
    while x<= len(ints)-1:
        for num in range(0, x):
            if ints[num] + ints[x] == s:
                return [ints[num], ints[x]]
        x += 1
    return None

def f7(seq):
    new_list = []
    for x in seq:
        if new_list.count(x) < 2:
            new_list.append(x)
    return  new_list






"""def sum_pairs(ints, s):
    x = 1

    while x < (2*len(ints))-3:


        if x < 3:
            if ints[0] + ints[1] == s:
                return [ints[0], ints[1]]
            elif ints[0] + ints[2] == s:
                return [ints[0], ints[0]]
        elif x >= 3:

            n = 0
            if x % 2 != 0:
                inx = x//2

                while inx + 1 + n <= x:
                    print([inx - n, inx + 1 + n])
                    if inx + 1 + n > len(ints)-1:
                        break
                    if ints[inx - n] + ints[inx + 1 + n] == s:

                        return [ints[inx - n], ints[inx + 1 + n]]
                    n += 1
            else:
                inx = (x//2) - 1

                while inx + 2 + n <= x:
                    print([inx - n, inx + 2 + n])
                    if inx + 2 + n > len(ints)-1:
                        break
                    if ints[inx - n] + ints[inx + 2 + n] == s:

                        return [ints[inx - n], ints[inx + 2 + n]]
                    n += 1


        x+= 1
    return None"""