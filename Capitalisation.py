# Better solution
def fix(paragraph):
    return '. '.join(s.capitalize() for s in paragraph.split('. '))


def fix(paragraph):
    cap =True
    output = ""
    for letter in paragraph:
        if letter == '.':
            output += letter
            cap = True
            continue
        elif cap:
            if letter == ' ':
                output += letter
                continue
            else:
                output += letter.upper()
                cap = False
        else:
            output += letter

    return output

print(fix("hello. my name is inigo montoya. you killed my father. prepare to die."))

