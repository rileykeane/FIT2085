import unsorted_list_ADT as list_ADT


def initialise_tour(n):
    """
    Create a tour data type of size n

    @param      n: the size of the tour n*n
    @return     the tour data type
    @post       the tour will initially be empty and can be populated using other tour functions
    @complexity best and worst case: O(n^2) where n is in input n
    """

    tour = list_ADT.List(n*n)
    return tour


def print_tour(tour):
    """
    This will print a chess board representation of the tour

    @param      tour: the tour data type
    @post       the printed board will have non visited positions as 0, visited at * and the current as K
    @complexity best and worst: O(n^2) where n is the length of the tour
    """
    n = int(list_ADT.size(tour)**0.5)

    # creating a chess board of size n*n
    board = list_ADT.List(n)
    # populating the board with 0s
    for _ in range(n):
        row = list_ADT.List(n)
        for _ in range(n):
            list_ADT.add_last(row, 0)
        list_ADT.add_last(board, row)

    # setting previous positions in board to '*'s
    n = list_ADT.length(tour)
    for i in range(n):
        pos = list_ADT.get_item(tour, i)
        # getting row and column of position
        pos_r = list_ADT.get_item(pos, 0) - 1
        pos_c = list_ADT.get_item(pos, 1) - 1
        # setting previous positions to a * and current to a K in board
        row = list_ADT.get_item(board, pos_r)
        if i == n-1:
            list_ADT.set_item(row, pos_c, 'K')
        else:
            list_ADT.set_item(row, pos_c, '*')

    # printing the tour
    print('\nCurrent Tour')
    n = list_ADT.length(board)
    col_numbers = ''
    for i in range(n, 0, -1):
        col_numbers = ' ' + str(i) + col_numbers
        row = list_ADT.get_item(board, i - 1)
        row_str = str(i) + '  '
        for j in range(list_ADT.length(row)):
            row_elt = list_ADT.get_item(row, j)
            row_str += str(row_elt) + ' '
        print(row_str)
    print('\n  ' + col_numbers)


def new_position(tour, row, col):
    """
    This adds a new position to the tour

    @param      tour: a tour data_type
    @param      row: the row of the position as an integer
    @param      col: the column of the position as an integer
    @return     True if the tour has space left, otherwise False
    @pre        row and col must be integers
    @pre        the tour must not be full
    @pre        the position must be within the size of the tour
    @post       the new position will be added to the end of the tour and will be treated as
                current position for all other tour functions
    @complexity best and worst case: O(1)
    """
    # checking the tour is not full
    if list_ADT.is_full(tour):
        raise Exception("The tour is complete. No more moves can be made")

    # checking row and col and integers
    try:
        int(row)
        int(col)
    except ValueError:
        raise ValueError('row and/or col must be integer values')

    # checking row and col fit into the tour
    n = int(list_ADT.size(tour)**0.5)
    if not (1 <= row <= n or 1 <= col <= n):
        raise IndexError('Row and/or col does not fit within the size of the tour')

    pos = list_ADT.List(2)
    list_ADT.add_last(pos, row)
    list_ADT.add_last(pos, col)
    list_ADT.add_last(tour, pos)

    if list_ADT.is_full(tour):
        return False
    else:
        return True


def next_moves(tour):
    """
    returns all the possible next moves for the tour

    @param      tour: a tour data data
    @return     a list of all possible next moves
    @pre        the tour must have made at least one move
    @post       only moves that have not already been made will be returned
    @post       only moves that are within the size of the tour will be returned
    @complexity best and worst case: O(n) where n is the length of the tour
    """
    # checking the tour has at least one move
    n = list_ADT.length(tour)
    if n == 0:
        raise Exception('The tour must have made at least one move')

    # getting current
    current_pos = list_ADT.length(tour) - 1
    current = list_ADT.get_item(tour, current_pos)

    # calculating all the next moves
    moves = list_ADT.List(8)

    move = list_ADT.List(2)
    list_ADT.add_last(move, list_ADT.get_item(current, 0) + 2)
    list_ADT.add_last(move, list_ADT.get_item(current, 1) + 1)
    list_ADT.add_last(moves, move)

    move = list_ADT.List(2)
    list_ADT.add_last(move, list_ADT.get_item(current, 0) + 2)
    list_ADT.add_last(move, list_ADT.get_item(current, 1) - 1)
    list_ADT.add_last(moves, move)

    move = list_ADT.List(2)
    list_ADT.add_last(move, list_ADT.get_item(current, 0) - 2)
    list_ADT.add_last(move, list_ADT.get_item(current, 1) + 1)
    list_ADT.add_last(moves, move)

    move = list_ADT.List(2)
    list_ADT.add_last(move, list_ADT.get_item(current, 0) - 2)
    list_ADT.add_last(move, list_ADT.get_item(current, 1) - 1)
    list_ADT.add_last(moves, move)

    move = list_ADT.List(2)
    list_ADT.add_last(move, list_ADT.get_item(current, 0) + 1)
    list_ADT.add_last(move, list_ADT.get_item(current, 1) - 2)
    list_ADT.add_last(moves, move)

    move = list_ADT.List(2)
    list_ADT.add_last(move, list_ADT.get_item(current, 0) + 1)
    list_ADT.add_last(move, list_ADT.get_item(current, 1) + 2)
    list_ADT.add_last(moves, move)

    move = list_ADT.List(2)
    list_ADT.add_last(move, list_ADT.get_item(current, 0) - 1)
    list_ADT.add_last(move, list_ADT.get_item(current, 1) - 2)
    list_ADT.add_last(moves, move)

    move = list_ADT.List(2)
    list_ADT.add_last(move, list_ADT.get_item(current, 0) - 1)
    list_ADT.add_last(move, list_ADT.get_item(current, 1) + 2)
    list_ADT.add_last(moves, move)

    # checking moves are valid
    n_tour = list_ADT.length(tour)
    valid_moves = list_ADT.List(8)

    for j in range(8):
        move = list_ADT.get_item(moves, j)
        move_r = list_ADT.get_item(move, 0)
        move_c = list_ADT.get_item(move, 1)
        tour_size = int(list_ADT.size(tour)**0.5)

        # comparing move to previous moves
        previous_move = False
        i = 0
        while not previous_move and i < n_tour:
            pos = list_ADT.get_item(tour, i)
            if move == pos:
                previous_move = True
            i += 1

        # checking if move has not already been made and if the move fits within the tour
        if 1 <= move_r <= tour_size and 1 <= move_c <= tour_size and not previous_move:
            list_ADT.add_last(valid_moves, move)

    return valid_moves


def undo_move(tour):
    """
    undo the last move on the tour

    @param      tour: a tour data type
    @pre        the tour must have made at least one move.
    @post       the previous move will become the current move of the tour
    @return     True if the move is successfully deleted
    @complexity best and worst case: O(1)
    """
    n = list_ADT.length(tour)

    if n > 0:
        list_ADT.delete_last(tour)
        return True
    else:
        raise Exception('The tour must have made at least one move')


def check_position(tour, r, c):
    """
    checks that the imputed position is a valid move for a knight

    @param      tour: a tour data type
    @param      r: the row of the position to be tested
    @param      c: the column of the position to be tested
    @pre        the tour must have made at least one move
    @post       r and c must be integers
    complexity  best and worst case: O(1)
    """
    # handling errors from next_moves
    try:
        possible_moves = next_moves(tour)
    except Exception:
        print('The tour must have made at least one move')

    # checking row and col and integers
    try:
        int(r)
        int(c)
    except ValueError:
        raise ValueError('row and/or col must be integer values')

    # creating a list ADT for new move
    new = list_ADT.List(2)
    list_ADT.add_last(new, r)
    list_ADT.add_last(new, c)

    for i in range(list_ADT.length(possible_moves)):
        move = list_ADT.get_item(possible_moves, i)
        if new == move:
            return True

    return False


def next_moves_str(moves):
    """
    Returns next moves as a string

    @param      moves: the next moves for the tour generated with next_moves
    @return     a string containing all the moves in the form r1,c1; r2,c2;...
    @complexity best and worst case: O(1)
    """
    moves_str = ""
    for i in range(list_ADT.length(moves)):
        move = list_ADT.get_item(moves, i)
        moves_str += str(list_ADT.get_item(move, 0)) + ',' + str(list_ADT.get_item(move, 1)) + '; '
    return moves_str
