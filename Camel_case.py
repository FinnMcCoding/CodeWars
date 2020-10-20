
def to_camel_case(text):
    if '_' in text or '-' in text:
        output = ''
        _count = 0
        for letter in text:

            if letter != '_' and letter != '-':
                if _count == 0:
                    output += letter
                elif _count == 1:
                    output += letter.upper()
                    _count = 0
            else:
                _count = 1
                pass
        return output
    else:
        return ''

print(to_camel_case("the-stealth-Warrior"))
