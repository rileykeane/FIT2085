import unsorted_list_ADT as list_ADT


def initialise_tour(n):
    """
    Initialise a tour of size n X n with all positions set to 0

    @param: n:       the size of the tour
    @return          the tour as a list ADT
    @complexity      best and worst case: O(n^2) where n is the param n
    @pre-conditions: n must be an integer > 0
    @post-condition: a list ADT where each element is another list ADT repressing each row of the tour. the first item
                     is row 1 and so on.
    """
    tour = list_ADT.List(n)

    for _ in range(n):
        row = list_ADT.List(n)
        for _ in range(n):
            list_ADT.add_last(row, 0)
        list_ADT.add_last(tour, row)

    return tour


def print_tour(tour):
    """
    Prints the tour in the format of a chessboard

    @param: tour:    a tour created with the initialise_tour function
    @return          N/A
    @complexity      best and worst case: O(n^2) where n is the length of the tour
    @pre-conditions: imputed tour must be created using initialise_tour
    @post-condition: the function will print each row of the inputted tour in the format of a chessboard
    """
    print('\nCurrent Tour')
    n = list_ADT.length(tour)
    col_numbers = ''
    for i in range(n, 0, -1):
        col_numbers = ' ' + str(i) + col_numbers
        row = list_ADT.get_item(tour, i-1)
        row_str = str(i) + '  '
        for j in range(list_ADT.length(row)):
            row_elt = list_ADT.get_item(row, j)
            row_str += str(row_elt) + ' '
        print(row_str)
    print('\n  ' + col_numbers)


def new_position(tour, new, current):
    """
    Changes given position on tour to a K and previous position to a *

    @param: tour:    a tour created with the initialise_tour function
    @param: new:     a list ADT with the row x column of the new position
    @param: current: a list adt with the row x column of the current position
    @return          The tour with the new position changed to a K and current a *
    @complexity      best and worst case: O(1)
    @pre-conditions: new and current must both be list ADTs in the form [2, [r x c]] where r is the row as an integer
                     and c is the column as an integer. The value for both r and c must fall within 1 and n where n is
                     the length of the tour.
    @post-condition: the function will return the tour with the new changed to a K and current changed to a *. The rest
                     of the tour will remain the same.
    """

    if current is not None:
        current_r = list_ADT.get_item(current, 0) - 1
        current_c = list_ADT.get_item(current, 1) - 1
        try:
            # setting  the current position on the tour to a *
            row = list_ADT.get_item(tour, current_r)
            list_ADT.set_item(row, current_c, '*')
        except (IndexError, ValueError, AssertionError):
            raise IndexError('current does not fall within tour size')

    new_r = list_ADT.get_item(new, 0) - 1
    new_c = list_ADT.get_item(new, 1) - 1
    try:
        # setting the new position on the tour to a 'K'
        row = list_ADT.get_item(tour, new_r)
        list_ADT.set_item(row, new_c, 'K')
    except (IndexError, ValueError, AssertionError):
        raise IndexError('new does not fall within tour size')

    return tour


def next_moves(tour, current):
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
    board_length = list_ADT.length(tour)
    valid_moves = list_ADT.List(8)

    for i in range(list_ADT.length(moves)):
        move = list_ADT.get_item(moves, i)
        move_r = list_ADT.get_item(move, 0)
        move_c = list_ADT.get_item(move, 1)

        if 1 <= move_r <= board_length and 1 <= move_c <= board_length:
            tour_row = list_ADT.get_item(tour, move_r - 1)
            if list_ADT.get_item(tour_row, move_c - 1) != '*':
                valid = list_ADT.List(2)
                list_ADT.add_last(valid, move_r)
                list_ADT.add_last(valid, move_c)
                list_ADT.add_last(valid_moves, valid)

    return valid_moves


def check_position(tour, pos, moves):
    # Checking position is valid
    if moves is not None:
        for i in range(list_ADT.length(moves)):
            if list_ADT.get_item(moves, i) == pos:
                return True
    else:
        n = list_ADT.length(tour)
        if 1 <= list_ADT.get_item(pos, 0) <= n and 1 <= list_ADT.get_item(pos, 1) <= n:
            return True
    return False

