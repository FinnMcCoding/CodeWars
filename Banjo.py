def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return f'{name} plays banjo'
    else:
        return f'{name} does not play banjo'

print(areYouPlayingBanjo(input('name here: ')))