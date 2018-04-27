from tour import initialise_tour, print_tour, new_position, next_moves, undo_move, check_position, next_moves_str
import unsorted_list_ADT as list_ADT


def test_initialise_tour():
    assert initialise_tour(8) == [0, [None]*64]
    assert initialise_tour(3) == [0, [None]*9]
    assert initialise_tour(12) == [0, [None]*144]
    print('initialise_tour passed all tests')


def test_print_tour():
    test_tour1 = initialise_tour(8)
    print_tour(test_tour1)
    list_ADT.add_last(test_tour1, [2, [4, 4]])
    print_tour(test_tour1)
    list_ADT.add_last(test_tour1, [2, [6, 5]])
    list_ADT.add_last(test_tour1, [2, [5, 7]])
    print_tour(test_tour1)


def test_new_position():
    test_tour1 = initialise_tour(2)
    assert new_position(test_tour1, 1, 1)
    assert new_position(test_tour1, 1, 2)
    assert new_position(test_tour1, 2, 1) is True
    assert new_position(test_tour1, 2, 2) is False
    print('new_position passed all tests')


def test_next_moves():
    test_tour1 = initialise_tour(8)
    new_position(test_tour1, 4, 4)
    assert next_moves(test_tour1) == [8, [[2, [6, 5]], [2, [6, 3]], [2, [2, 5]], [2, [2, 3]], [2, [5, 2]], [2, [5, 6]], [2, [3, 2]], [2, [3, 6]]]]
    new_position(test_tour1, 6, 5)
    assert next_moves(test_tour1) == [7, [[2, [8, 6]], [2, [8, 4]], [2, [4, 6]], [2, [7, 3]], [2, [7, 7]], [2, [5, 3]], [2, [5, 7]], None]]
    new_position(test_tour1, 8, 6)
    assert next_moves(test_tour1) == [3, [[2, [6, 7]], [2, [7, 4]], [2, [7, 8]], None, None, None, None, None]]
    print('next_moves passed all tests')


def test_undo_move():
    test_tour1 = initialise_tour(8)
    new_position(test_tour1, 4, 4)
    new_position(test_tour1, 6, 5)
    assert undo_move(test_tour1) is True
    assert list_ADT.get_item(test_tour1, list_ADT.length(test_tour1) - 1) == [2, [4, 4]]
    assert undo_move(test_tour1) is True
    print('undo_move passed all tests')


def test_check_position():
    test_tour1 = initialise_tour(8)
    new_position(test_tour1, 4, 4)
    assert check_position(test_tour1, 6, 5) is True
    new_position(test_tour1, 6, 5)
    assert check_position(test_tour1, 8, 8) is False
    assert check_position(test_tour1, 7, 7) is True
    print('check_position passed all tests')


def test_next_moves_str():
    test_tour1 = initialise_tour(8)
    new_position(test_tour1, 4, 4)
    moves = next_moves(test_tour1)
    print(next_moves_str(moves))


test_initialise_tour()
test_new_position()
test_next_moves()
test_undo_move()
test_check_position()

test_print_tour()
test_next_moves_str()
