import tour


def test_initialise_tour():
    test_cases = [
        (2, [2, [[2, [0, 0]], [2, [0, 0]]]]),
        (4, [4, [[4, [0, 0, 0, 0]], [4, [0, 0, 0, 0]], [4, [0, 0, 0, 0]], [4, [0, 0, 0, 0]]]]),
        (8, [8, [[8, [0, 0, 0, 0, 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]]]])
    ]

    for test, exp_result in test_cases:
        result = tour.initialise_tour(test)
        assert result == exp_result, 'Failed on {} - got {}, expected {}'.format(test, result, exp_result)

    print('Passed all tests')


def test_print_tour():
    print('testing 2 X 2 tour')
    my_tour = tour.initialise_tour(2)
    tour.print_tour(my_tour)
    print('\n\n')

    print('testing 4 X 4 tour')
    my_tour = tour.initialise_tour(4)
    tour.print_tour(my_tour)
    print('\n\n')

    print('testing 8 X 8 tour')
    my_tour = tour.initialise_tour(8)
    tour.print_tour(my_tour)
    print('\n\n')


def test_new_position():
    tour8 = tour.initialise_tour(8)

    tests = [
        (1, tour8, [2, [4, 4]], None, [8, [[8, [0, 0, 0, 0, 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]], [8, [0, 0, 0, 'K', 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]]]]),
        (2, tour8, [2, [2, 3]], [2, [4, 4]], [8, [[8, [0, 0, 0, 0, 0, 0, 0, 0]], [8, [0, 0, 'K', 0, 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]], [8, [0, 0, 0, '*', 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]]]]),
        (3, tour8, [2, [1, 5]], [2, [2, 3]], [8, [[8, [0, 0, 0, 0, 'K', 0, 0, 0]], [8, [0, 0, '*', 0, 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]], [8, [0, 0, 0, '*', 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]], [8, [0, 0, 0, 0, 0, 0, 0, 0]]]])
    ]

    for test_no, the_tour, new, current, exp_result in tests:
        result = tour.new_position(the_tour, new, current)
        assert result == exp_result, 'Failed on {}, {}, {} - got {}, expected {}'.format(test_no, current, new, result, exp_result)
    print('Passed all tests')


def test_check_position():
    the_tour = tour.initialise_tour(8)
    tour.new_position(the_tour, [2, [4, 4]], None)
    valid_moves = tour.next_moves(the_tour, [2, [4, 4]])
    assert tour.check_position(the_tour, [2, [4, 4]], valid_moves) is False
    assert tour.check_position(the_tour, [2, [7, 7]], valid_moves) is False
    assert tour.check_position(the_tour, [2, [29, 18]], valid_moves) is False
    assert tour.check_position(the_tour, [2, [2, 5]], valid_moves) is True
    print('Passed all tests')


test_check_position()