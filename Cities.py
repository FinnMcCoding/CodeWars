import re

def get_strings(city):
    city = re.sub('[^a-zA-Z]+', '', city).lower()
    counted = []
    output = ""
    for letter in city:
        if letter in counted:
            continue
        else:
            count = city.count(letter)
            output += letter.lower() + ':' + count * '*' + ','
            counted.append(letter)

    return output[:-1]