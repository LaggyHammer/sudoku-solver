def valid_move(board, row, column, input_number):
    # Check Row
    for position in range(len(board)):
        if board[row][position] == input_number and column != position:
            return False

    # Check Column
    for position in range(len(board)):
        if board[position][column] == input_number and row != position:
            return False

    # Check Box (3x3)
    box_row = row // 3
    box_column = column // 3

    for column_position in range(box_column * 3, box_column * 3 + 3):
        for row_position in range(box_row * 3, box_row * 3 + 3):
            if board[row_position][column_position] == input_number and (row_position, column_position) != (
                    row, column):
                return False

    return True


def empty_position(board):
    for row_position in range(len(board)):
        for column_position in range(len(board)):
            if board[row_position][column_position] == 0:
                return row_position, column_position

    return None


def print_board(board):
    for row in range(len(board)):

        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - - - -")

        for column in range(len(board[row])):

            if column % 3 == 0:
                print(" | ", end="")
            if column == len(board[row]) - 1:
                print(board[row][column], end="\n")
            else:
                print(str(board[row][column]) + " ", end="")

    return None


def solve_sudoku(board):
    empty_pos = empty_position(board)
    if empty_pos:
        row, col = empty_pos
    else:
        print("Solved Sudoku Puzzle")
        print_board(board)
        return True

    for number in range(1, 10):
        if valid_move(board, row, col, number):
            board[row][col] = number

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


def puzzle_solver(board):
    print("Input Sudoku Puzzle")
    print_board(board)
    solve_sudoku(board)


board1 = [

    [7, 8, 0, 4, 0, 0, 1, 2, 0],

    [6, 0, 0, 0, 7, 5, 0, 0, 9],

    [0, 0, 0, 6, 0, 1, 0, 7, 8],

    [0, 0, 7, 0, 4, 0, 2, 6, 0],

    [0, 0, 1, 0, 5, 0, 9, 3, 0],

    [9, 0, 4, 0, 6, 0, 0, 0, 5],

    [0, 7, 0, 3, 0, 0, 0, 1, 2],

    [1, 2, 0, 0, 0, 7, 4, 0, 0],

    [0, 4, 9, 2, 0, 6, 0, 0, 7]

]

puzzle_solver(board1)
