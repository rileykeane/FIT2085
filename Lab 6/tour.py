import unsorted_list_ADT as list_ADT


def initialise_board(n):
    board = list_ADT.List(n)

    for _ in range(n):
        row = list_ADT.List(n)
        for _ in range(n):
            list_ADT.add_last(row, 0)
        list_ADT.add_last(board, row)

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


def next_moves(board, current):
    moves = list_ADT.List(8)

    move = list_ADT.List(2)
    list_ADT.add_last(move, current[1][0] + 2)
    list_ADT.add_last(move, current[1][1] + 1)
    list_ADT.add_last(moves, move)

    move = list_ADT.List(2)
    list_ADT.add_last(move, current[1][0] + 2)
    list_ADT.add_last(move, current[1][1] - 1)
    list_ADT.add_last(moves, move)

    move = list_ADT.List(2)
    list_ADT.add_last(move, current[1][0] - 2)
    list_ADT.add_last(move, current[1][1] + 1)
    list_ADT.add_last(moves, move)

    move = list_ADT.List(2)
    list_ADT.add_last(move, current[1][0] - 2)
    list_ADT.add_last(move, current[1][1] - 1)
    list_ADT.add_last(moves, move)

    move = list_ADT.List(2)
    list_ADT.add_last(move, current[1][0] + 1)
    list_ADT.add_last(move, current[1][1] - 2)
    list_ADT.add_last(moves, move)

    move = list_ADT.List(2)
    list_ADT.add_last(move, current[1][0] + 1)
    list_ADT.add_last(move, current[1][1] + 2)
    list_ADT.add_last(moves, move)

    move = list_ADT.List(2)
    list_ADT.add_last(move, current[1][0] - 1)
    list_ADT.add_last(move, current[1][1] - 2)
    list_ADT.add_last(moves, move)

    move = list_ADT.List(2)
    list_ADT.add_last(move, current[1][0] - 1)
    list_ADT.add_last(move, current[1][1] + 2)
    list_ADT.add_last(moves, move)

    # checking moves are valid
    board_length = list_ADT.length(board)
    for i in range(list_ADT.length(moves)):
        if moves[1][i][1][0] > board_length or moves[1][i][1][0] < 1 or moves[1][i][1][1] > board_length \
                or moves[1][i][1][1] < 1:
            moves[1][i] = None

    for i in range(list_ADT.length(moves)):
        if moves[1][i] is not None:
            move_r = moves[1][i][1][0] - 1
            move_c = moves[1][i][1][1] - 1
            if board[1][move_r][1][move_c] == '*':
                moves[1][i] = None

    valid_moves = list_ADT.List(8)
    for i in range(list_ADT.length(moves)):
        if moves[1][i] is not None:
            move = list_ADT.List(2)
            list_ADT.add_last(move, moves[1][i][1][0])
            list_ADT.add_last(move, moves[1][i][1][1])
            list_ADT.add_last(valid_moves,move)

    return valid_moves


