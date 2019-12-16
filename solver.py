def valid_move(board, row_column, input_number):
    row, column = row_column

    # Check Row
    for position in range(len(board)):
        if board[row][position] == input_number and position != column:
            return False

    # Check Column
    for position in range(len(board)):
        if board[position][column] == input_number and position != row:
            return False

    # Check Box (3x3)
    box_row = row // 3
    box_column = column // 3
    for column_position in range(box_column, box_column + 3):
        for row_position in range(box_row, box_row + 3):
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


print_board([[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5],
             [6, 6, 6, 6, 6, 6]])
