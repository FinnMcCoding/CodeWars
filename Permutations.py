import math

def permutations(string, output = []):
    if len(string) == 1:
        return [string]
    i = 0
    out = []
    for letter in string:
        shorter_str = ''.join(string[:i] + string[i+1:])

        for letters in permutations(shorter_str):
            out.append(letter+letters)

        i += 1
    return list(set(out))


print(permutations('aabb'))