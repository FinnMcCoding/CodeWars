
def dirReduc(arr):

    finished =False
    while not finished:
        finished = True
        print(arr)
        for n in range(0,len(arr)-1):
            if arr[n] == 'NORTH' and arr[n+1] == 'SOUTH':
                del arr[n]
                del arr[n]
                finished = False

                break
            elif arr[n] == 'SOUTH' and arr[n+1] == 'NORTH':
                del arr[n]
                del arr[n]
                finished = False

                break
            elif arr[n] == 'WEST' and arr[n+1] == 'EAST':
                del arr[n]
                del arr[n]
                finished = False

                break
            elif arr[n] == 'EAST' and arr[n+1] == 'WEST':

                del arr[n]
                del arr[n]
                finished = False

                break

    return arr


dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])