

def pig_it(text):
    words = text.split()
    print(words)
    pig_words = []
    for word in words:
        if word in '?!,':
            pig_words.append(word)
        else:
            word = word[1:] + word[0] + 'ay'
            pig_words.append(word)

    output = ' '.join(pig_words)

    return output


pig_it('the cat went to')