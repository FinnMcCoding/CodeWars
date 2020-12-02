
def valid_parentheses(string):
    open_count = 0
    for letter in string:
        if letter == '(':
            open_count += 1
        elif letter == ')':
            open_count -= 1
        if open_count < 0:
            return False
    if open_count == 0:
        return True
    else:
        return False
