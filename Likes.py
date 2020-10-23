
def likes(arry):
    no_likes = len(arry)
    if no_likes == 0:
        return 'no one likes this'
    elif no_likes == 1:
        return f'{arry[0]} likes this'
    elif no_likes ==2:
        return f'{arry[0]} and {arry[1]} like this'
    elif no_likes == 3:
        return f'{arry[0]},{arry[1]} and {arry[2]} like this'
    else:
        res = no_likes - 2
        return f'{arry[0]}, {arry[1]} and {res} others like this'

print(likes([]))
print(likes(['John']))
print(likes(['John', 'Mark']))
print(likes(['John', 'Mark', 'Jacob', 'Mary']))