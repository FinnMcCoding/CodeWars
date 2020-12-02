
def solution(string,markers):
    output = ''
    clear = False
    for letter in string:
        print(letter)
        if letter in markers:
            clear = True
        elif letter == '\n':
            clear = False
            try:
                if output[-1] == ' ':
                    output = output[:-1]
            except IndexError:
                pass
        if not clear:
            output += letter

    if output != '':
        return  output.strip(' ')
    else:
        return output

print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))