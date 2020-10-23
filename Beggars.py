def beggars(values, n):
    output = []
    for number in range(0,n):
        sum = 0
        i = 0
        while number+(i + 1) <= len(values):
            sum += values[number+i]
            i += n
        output.append(sum)
    return output

print(beggars([1,2,3,4,5], 2))



