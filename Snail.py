
def snail(snail_map):
    output = []
    if snail_map == []:
        return []
    elif len(snail_map) == 1:
        return snail_map[0]
    elif len(snail_map) == 2:
        output.append(snail_map[0][0])
        output.append(snail_map[0][1])
        output.append(snail_map[1][1])
        output.append(snail_map[1][0])
        return output

    if len(snail_map[0]) > 2:
        for num in snail_map[0]:
            output.append(num)
        for row in snail_map[1:]:
            output.append(row[-1])
        for num in reversed(snail_map[-1][:(len(snail_map[-1])-1)]):
            output.append(num)
        for row in reversed(snail_map[1:-1]):
            output.append(row[0])

        if len(snail_map[0]) == 3:
            output.append(snail_map[1][1])
            return output
        elif len(snail_map[0]) == 4:
            output.append(snail_map[1][1])
            output.append(snail_map[1][2])
            output.append(snail_map[2][2])
            output.append(snail_map[2][1])
            return output
        else:
            new_map  = []
            for row in snail_map:
                new_map.append(row[1:-1])
            new_map = new_map[1:-1]
            return [*output, *snail(new_map)]








array = [[1, 2, 3, 4 ,5],
         [6, 7, 8, 9, 10],
         [11,12,13,14,15],
         [16,17,18,19,20],
         [21,22,23,24,25]]
a = snail(array)
print(a)
