from functools import reduce

def product_array(numbers):
    output = []
    i = 0
    for num in numbers:
        short_list = numbers[:i]+numbers[i+1:]
        output.append(reduce((lambda x, y: x * y), short_list))
        i +=1
    return output

print(product_array([3,27,4,2]))