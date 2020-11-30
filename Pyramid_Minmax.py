

def longest_slide_down(pyramid):
    search_depth = 100
    current_loc = [0,0]
    sum = pyramid[0][0]
    pyra_height = len(pyramid)-1

    while current_loc[0] < pyra_height and search_depth > 1:

        p = []
        z = 0
        for line in enumerate(pyramid):
            if line[0] >= current_loc[0] and line[0] <= current_loc[0] + search_depth:

                p.append(line[1][current_loc[1]:current_loc[1]+z+1])

                z+=1
        if current_loc[0]+search_depth <= pyra_height:
            current_loc[0], current_loc[1] = solve_one(p,search_depth,current_loc)
            sum += pyramid[current_loc[0]][current_loc[1]]
        else:
            search_depth -= 1

    last_vals = pyramid[current_loc[0]+1][current_loc[1]],pyramid[current_loc[0]+1][current_loc[1]+1]
    if last_vals[0] > last_vals[1]:
        return sum + last_vals[0]
    else:
        return sum + last_vals[1]


def solve_one(curr_pyramid, curr_search_depth,current_loc):
    ref_line = [''] * curr_search_depth

    x = 0
    for root in curr_pyramid[curr_search_depth - 1]:
        base_val = 0
        for foot in curr_pyramid[curr_search_depth][x:x + 2]:

            val = root + foot

            if val > base_val:
                ref_line[x] = val
                base_val = val

        x += 1


    if len(ref_line) != 2:
        new_pyra = curr_pyramid.copy()
        new_pyra = new_pyra[:-2]
        new_pyra.append(ref_line)

        return solve_one(new_pyra,curr_search_depth-1,current_loc)
    else:
        if ref_line[0] > ref_line[1]:

            return [current_loc[0]+1,current_loc[1]]
        else:
            return [current_loc[0]+1,current_loc[1]+1]


