from collections import Counter
def find_it(seq):
    occurrence = Counter(seq)
    for key in occurrence:
        if occurrence[key]%2 !=0:
            return key
        else:
            pass
    return None