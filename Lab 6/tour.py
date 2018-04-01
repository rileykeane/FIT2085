import unsorted_list_ADT


def initialise_board(n):
    board = unsorted_list_ADT.List(n)

    for _ in range(n):
        row = unsorted_list_ADT.List(n)
        for _ in range(n):
            unsorted_list_ADT.add_last(row, 0)
        unsorted_list_ADT.add_last(board, row)

    return board


def print_board(board):
    print('\nCurrent Chessboard')
    for i in range(board[0], 0, -1):
        row = str(i) + '  '
        for j in range(board[1][i-1][0]):
            if board[1][i-1][1][j] is not None:
                row += str(board[1][i-1][1][j]) + ' '
            else:
                row += '  '
        print(row)

    col_numbers = '\n   '
    for i in range(board[0]):
        col_numbers += str(i+1) + ' '
    col_numbers += '\n'
    print(col_numbers)


def new_position(board, new, current):

    if current is not None:
        current_r = current[1][0] - 1
        current_c = current[1][1] - 1
        board[1][current_r][1][current_c] = '*'

    new_r = new[1][0] - 1
    new_c = new[1][1] - 1
    board[1][new_r][1][new_c] = 'K'

