
def array_leaders(numbers):
    i = 0
    output = []
    for num in numbers:
        sum_right = sum(numbers[i+1:])
        if sum_right < num:
            output.append(num)
        else:
            pass
        i +=1
    return output

print(array_leaders([1,2,3,4,0]))