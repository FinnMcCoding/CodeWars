# https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python

variable_vals = {0:[0,8],
                     1:[1,2,4],
                     2:[1,2,3,5],
                     3:[2,3,6],
                     4:[1,4,5,7],
                     5:[2,4,5,6,8],
                     6:[3,5,6,9],
                     7:[4,7,8],
                     8:[5,7,8,9,0],
                     9:[6,8,9]
                     }

def get_pins(observed):

    observed = str(observed)
    pin_list = list(map(str, variable_vals[int(observed[0])]))

    for i in range(1, len(observed)):
        pin_list = get_vals(pin_list, int(observed[i]))

    return pin_list




def get_vals(pin_list, next_num):
    new_pin_list = []
    for seq in pin_list:
        for num in variable_vals[next_num]:
            new_pin_list.append(seq + str(num))
    return new_pin_list


get_pins(11)
