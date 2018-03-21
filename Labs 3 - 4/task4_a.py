"""
@author Riley Keane
@since 13/3/18
@modified 21/3/18
"""
import random


def bubble_sort(the_list):
    """
    This function uses the bubble sort algorithm to sort a list (the_list) and returns the list in ascending order
    :param the_list: A list of integers
    :return: The same list of integers, sorted in acceding order
    :pre-condition: The list given to the function must be of orderable elements, that is it can't be numbers and
    strings, it must be the same.
    :post-condition: This function will sort the list  in ascending that is inputted into the function and also return
    the sorted list in ascending order
    """
    # Set the list to not be sorted
    sorted = False

    # while the list is not sorted keep looping
    while not sorted:
        list_length = len(the_list)
        # setting the counter
        i = 0
        sorted = True
        # Loop through the list
        while i < list_length - 1:
            # If the first item is larger then then the second swap them
            if the_list[i] > the_list[i + 1]:
                # performing a swap
                temp = the_list[i]
                the_list[i] = the_list[i + 1]
                the_list[i + 1] = temp
                # setting the list to not sorted
                sorted = False
            # counter incrementer
            i = i + 1
    return the_list


def test_bubble_sort():
    """
    This function tests the bubble sort function by generating a list of 50 random integers and sorts them using the
    bubble sort function and pythons built in sort function. It then checks both methods get the same result. It also
    runs the same test for some other defined non random tests
    :return: An assert if a test fails
    """
    random_vals = []

    # generating 50 random integers between 0 and 100 and appending them to a list
    for i in range(50):
        random_vals.append(random.randrange(0, 100, 1))

    # Creating a copy of the random values list and sorting using pythons built in method
    py_sort = random_vals[:]
    py_sort.sort()

    # test cases
    tests = [
        (random_vals, py_sort),
        ([], []),
        ([1], [1]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])
    ]

    # looping through each test case and running each test
    for test, expected in tests:
        result = test[:]
        result = bubble_sort(result)
        assert result == expected, 'Failed on {} - got {}, expected {}'.format(test, result,expected)
