def solve(row_count, column_count, puzzle):

    short_puzz = puzzle
    # Reducing rows down
    if 0 <= row_count <= 2:
        short_puzz = short_puzz[0:3]
        row_amend = row_count
    elif 3 <= row_count <= 5:
        short_puzz = short_puzz[3:6]
        row_amend = row_count - 3
    elif 6 <= row_count <= 8:
        short_puzz = short_puzz[6:]
        row_amend = row_count - 6

    # Reducing columns down
    short_puzz_ref = short_puzz

    i = 0
    if 0 <= column_count <= 2:
        for row in short_puzz_ref:
            if i != row_amend:
                short_puzz[i] = row[0:3]
            i += 1
    elif 3 <= column_count <= 5:
        for row in short_puzz_ref:
            if i != row_amend:
                short_puzz[i] = row[3:6]
            i += 1
    elif 6 <= column_count <= 8:
        for row in short_puzz_ref:
            if i != row_amend:
                short_puzz[i] = row[6:]
            i += 1

    column_num = []
    for row in puzzle:
        column_num.append(row[column_count])
    short_puzz.append(column_num)

    reference_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for group in short_puzz:
        for num in group:
            if num in reference_num:
                reference_num.remove(num)
            else:
                pass
    print(reference_num)
    if len(reference_num) == 1:
        puzzle[row_count][column_count] = reference_num.pop(0)
        return puzzle
    else:
        #puzzle[row_count][column_count] = reference_num
        return puzzle

def sudoku(puzzle):
    global counter
    try:
        counter
    except NameError:
        counter = 0

    row_count = -1
    # Find the next empty cell and shows info on its location
    solved = True
    for row in puzzle:
        column_count = 0
        row_count += 1
        for num in row:
            if num == 0:
                puzzle  = solve(row_count, column_count, puzzle)
                column_count +=1
                solved = False
            else:
                column_count +=1
                pass

    if solved:
        return puzzle

    if counter <= 100:
        counter +=1
        return sudoku(puzzle)



"""puzzle = [[0, 4, 6, 0, 0, 0, 0, 0, 0],
          [9, 0, 2, 0, 6, 0, 0, 0, 8],
          [0, 0, 8, 4, 0, 0, 2, 5, 0],
          [0, 0, 0, 8, 0, 0, 0, 7, 0],
          [5, 0, 0, 7, 0, 2, 0, 0, 3],
          [0, 1, 0, 0, 0, 6, 0, 0, 0],
          [0, 6, 4, 0, 0, 3, 9, 0, 0],
          [3, 0, 0, 0, 8, 0, 1, 0, 2],
          [0, 0, 0, 0, 0, 0, 7, 3, 0]]
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]"""
puzzle = [[6, 0, 0, 1, 0, 8, 2, 0, 3], [0, 2, 0, 0, 4, 0, 0, 9, 0], [8, 0, 3, 0, 0, 5, 4, 0, 0], [5, 0, 4, 6, 0, 7, 0, 0, 9], [0, 3, 0, 0, 0, 0, 0, 5, 0], [7, 0, 0, 8, 0, 3, 1, 0, 2], [0, 0, 1, 7, 0, 0, 9, 0, 6], [0, 8, 0, 0, 3, 0, 0, 2, 0], [3, 0, 2, 9, 0, 4, 0, 0, 5]]
for row in sudoku(puzzle):
    print(row)
print(puzzle)