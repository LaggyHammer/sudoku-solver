def valid_move(board, row_column, input_number):
    row, column = row_column

    # Check Row
    for position in range(0, len(board)):
        if board[row][position] == input_number and position != column:
            return False

    # Check Column
    for position in range(0, len(board)):
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
    for row_position in len(board):
        for column_position in len(board):
            if board[row_position][column_position] == 0:
                return row_position, column_position

    return None
