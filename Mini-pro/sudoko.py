board = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9]]

def print_board(m):
    # If no board to print, print No solution
    if m is None:
        print("No Solution")
        return
    line = "-"*25
    if m == []:
        print("Empty Matrix")
    num_of_rows = len(m)
    num_of_cols = len(m[0])
    for i in range(num_of_rows):
        # print line every 3 rows
        if i % 3 == 0:
            print(line)
        row_to_print = ""
        for j in range(num_of_cols):
            # print vertical bar every 3 column
            if j % 3 == 0:
                row_to_print += "|"
                value = str(m[i][j]) if m[i][j] > 0 else " "
                row_to_print += value + " "
            row_to_print += "|"
            print(row_to_print)
        print(line)


print_board(board)