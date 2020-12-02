def alphabet_war(battlefield):
    print(battlefield)
    output = ''
    bunker_list = []
    bunker_count = 0
    if '#' not in battlefield:
        for letter in battlefield:
            if letter != '[' and letter != ']':
                output += letter
            else:
                pass
        return output
    elif '#' in battlefield:
        bunker = False
        for letter in battlefield:
            if letter == '[':
                bunker = True
                current_bunker = ''
                continue
            elif letter == ']':
                bunker = False
                bunker_list.append(current_bunker)
                bunker_count += 1
                continue
            else:
                if bunker == True:
                    current_bunker += letter
    alive_bunkers = nukes(battlefield)

    for bunker_num in alive_bunkers:
        output += bunker_list[bunker_num]
    return output



def nukes(battlefield):
    new_battlefield = ''
    for letter in battlefield:
        if letter in ['#','[',']']:
            new_battlefield += letter
    nuke_count_dict = {}
    nuke_count = 0
    bunker_count = 0
    for letter in new_battlefield:
        if letter == '#':
            nuke_count += 1
        if letter == '[':
            try:
                nuke_count_dict[bunker_count-1] += nuke_count
                nuke_count_dict[bunker_count] = nuke_count
            except KeyError:
                nuke_count_dict[bunker_count] = nuke_count
            nuke_count = 0
            bunker_count += 1

    if nuke_count != 0:
        nuke_count_dict[bunker_count-1] += nuke_count
    alive_bunkers = []

    for key in nuke_count_dict:
        if nuke_count_dict[key] < 2:
            alive_bunkers.append(key)
    return alive_bunkers



print(alphabet_war('##abde[fgh]i#jk[mn]op'))
