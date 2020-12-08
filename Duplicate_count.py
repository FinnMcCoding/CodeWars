
def duplicate_count(text):
    text_dict = {}
    for letter in text:
        try:
            text_dict[letter.upper()] += 1
        except KeyError:
            text_dict[letter.upper()] = 1
    output = []
    for key in text_dict:
        if text_dict[key] > 1:
            output.append(key)
    return len(output)


duplicate_count('abbccdd111')