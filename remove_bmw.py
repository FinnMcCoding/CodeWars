def remove_bmw(string):
    if type(string) != str:
        raise TypeError("This program only works for text.")
    output = ''
    for letter in string:

        if letter.upper() == 'B' or letter.upper() == 'M' or letter.upper() == 'W':
            pass
        else:
            output += letter
    return output




print(remove_bmw('abcbmw'))