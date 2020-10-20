import operator

symbols = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}

def zero(symbol=None, number=None): #your code here
    if symbol == None:
        return 0
    else:
        number = symbol[1]
        symbol = symbol[0]
        return symbols[symbol](0, number)
def one(symbol=None, number=None): #your code here
    if symbol == None:
        return 1
    else:
        number = symbol[1]
        symbol = symbol[0]
        return symbols[symbol](1, number)
def two(symbol=None, number=None): #your code here
    if symbol == None:
        return 2
    else:
        number = symbol[1]
        symbol = symbol[0]
        return symbols[symbol](2, number)
def three(symbol=None, number=None): #your code here
    if symbol == None:
        return 3
    else:
        number = symbol[1]
        symbol = symbol[0]
        return symbols[symbol](3, number)
def four(symbol=None, number=None): #your code here
    if symbol == None:
        return 4
    else:
        number = symbol[1]
        symbol = symbol[0]
        return symbols[symbol](4, number)
def five(symbol=None, number=None): #your code here
    if symbol == None:
        return 5
    else:
        number = symbol[1]
        symbol = symbol[0]
        return symbols[symbol](5, number)
def six(symbol=None, number=None): #your code here
    if symbol == None:
        return 6
    else:
        number = symbol[1]
        symbol = symbol[0]
        return symbols[symbol](6, number)
def seven(symbol=None, number=None): #your code here
    if symbol == None:
        return 7
    else:
        number = symbol[1]
        symbol = symbol[0]
        return symbols[symbol](7, number)
def eight(symbol=None, number=None): #your code here
    if symbol == None:
        return 8
    else:
        number = symbol[1]
        symbol = symbol[0]
        return symbols[symbol](8, number)
def nine(symbol=None, number=None): #your code here
    if symbol == None:
        return 9
    else:
        number = symbol[1]
        symbol = symbol[0]
        return symbols[symbol](9, number)

def plus(num): #your code here
    return '+',num
def minus(num): #your code here
    return '-', num
def times(num): #your code here
    return '*', num
def divided_by(num): #your code here
    return '/', num

print(seven(times(five())))