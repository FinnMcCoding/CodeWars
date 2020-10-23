from numpy import array
def dup(arry):
    output = []
    for string in arry:
        previous = ''
        i = 0
        word = ''
        for letter in string:
            if letter != previous:
                word = word + letter
            else:
                pass
            previous =letter
            i += 1
        output.append(word)
    return output
