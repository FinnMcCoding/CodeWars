group = {
    'A': 20,
    'B': 15,
    'C': 10
}

def split_the_bill(x):
    owed_dict = {}
    sum = 0
    people = 0
    for key in x:
        sum = sum + x[key]
        people = people + 1
    price_pp = sum/people
    for key in x:
        owed_value = x[key] - price_pp
        owed_dict[key] = round(owed_value, 2)
    return owed_dict


split_the_bill(group)