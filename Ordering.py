def order(string):
    string = string + ' '
    word = ''
    list = []
# Csan use string.split() here instead
    for letter in string:

        if letter != ' ':
            word += letter
        elif letter == ' ':
            list.append(word)
            word = ''
    output = ''
    i = 1
    while i <= len(list):
        if list == ['']:
            return ""
        for word in list:
            if str(i) in word and i == 1:
                output += word
                i +=1
            elif str(i) in word and i !=1:
                output = output + ' ' + word
                i+=1
            else:
                pass
    return output




print(order(''))