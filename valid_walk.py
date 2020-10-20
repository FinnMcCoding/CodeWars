def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    location = [0,0]
    for direction in walk:
        if direction == 'e':
            location[0] += 1
        elif direction == 'w':
            location[0] -= 1
        elif direction == 'n':
            location[1] += 1
        elif direction == 's':
            location[1] -= 1
    if location == [0,0]:
        return True
    else:
        return False




print(is_valid_walk(['e']*10))
