# Best Solution:
# def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]

def anagrams(word, words):
    word_dict, output = {}, []
    for letter in word:
        try:
            word_dict[letter] += 1
        except KeyError:
            word_dict[letter] = 1

    for set in words:
        ref_dict = {}
        if len(set) != len(word):
            continue
        else:
            for letter in set:
                try:
                    ref_dict[letter] += 1
                except KeyError:
                    ref_dict[letter] = 1
            if ref_dict == word_dict:
                output.append(set)
    return output

print(anagrams('aabb', ['bba']))