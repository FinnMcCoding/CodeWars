
# All you need to do is sort out the case using True and False
# This breaks at (1)

def josephus(items ,k):
    n = 1
    output = []
    while items != []:

        deleted_nums = []
        y = 0
        for num in items:
            if n % k == 0:
                deleted_nums.append(y)
                output.append(num)
            n += 1
            y += 1

        print(deleted_nums,items)
        z = 0
        for num in deleted_nums:
            del items[num-z]
            z+=1


    return output






print(josephus([1, 2, 3, 4, 5, 6, 7], 3))













"""
def josephus(items,k):
    i = 0
    output = []
    while len(items) != 1:
        for i in items[::k]:
            output.append(i)
    output.append(items[0])
    return output





    while len(items) != 1:
        for item in items:
            print(item)
            i += 1
            if i != k:
                pass
            elif i == k:

                output.append(item)
                items.remove(item)
                i = 0
    output.append(items[0])
    return output
"""
