
def score(dice):
    roll_dict = {'1':0, '2': 0, '3': 0, '4': 0, '5': 0, '6':0 }
    score = 0
    for roll in dice:
        roll_dict[str(roll)] += 1
    for key in roll_dict:
        if roll_dict[key] >= 3:
            if key != '1':
                score += 100*int(key)
            elif key == '1':
                score += 1000

        if key in ['1','5']:
            excess = roll_dict[key] % 3

            if key == '1':
                score += excess*100
            elif key == '5':
                score += excess*50
    return score

print(score([2, 4, 4, 5, 4] ))