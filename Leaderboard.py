def leaderboard_sort(leaderboard, changes):
    for move in changes:
        movement = move.split()
        indx = leaderboard.index(movement[0])
        if '+' in movement[1]:
            dist = int(movement[1].strip('+'))
            leaderboard.insert(indx-dist, leaderboard.pop(indx))
        else:
            dist = int(movement[1].strip('-'))
            leaderboard.insert(indx + dist, leaderboard.pop(indx))
    return leaderboard







print(leaderboard_sort(['John', 'Brian', 'Jim', 'Dave', 'Fred'], ['Dave +1', 'Fred +4', 'Brian -1']))