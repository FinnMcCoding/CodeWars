def add(num1, num2):
    i = 1
    sum = ''
    num1 = str(num1)
    num2 = str(num2)
    if len(num1) == len(num2):
        while i <= len(num1):
            added_value = int(num1[-i])+int(num2[-i])
            sum = str(added_value)+ sum
            i +=1
        return int(sum)

    elif len(num1) > len(num2):
        diff = len(num1)-len(num2)
        trim_num1 = num1[diff:]
        res = num1[:diff]
        while i <=len(num2):
            added_value = int(trim_num1[-i])+int(num2[-i])
            sum = str(added_value) + sum
            i +=1
        sum = res + sum
        return int(sum)

    elif len(num1) < len(num2):
        diff = len(num2)-len(num1)
        trim_num2 = num2[diff:]
        res = num2[:diff]
        while i <=len(num1):
            added_value = int(trim_num2[-i])+int(num1[-i])
            sum = str(added_value) + sum
            i +=1
        sum = res + sum
        return int(sum)

print(add(input('first num: '), input('second num: ')))

