"""
@author Riley Keane
@since 11/3/18
@modified 21/3/18
"""
import random


def read_list():
    """
    This function asks the user for the number of days in a month, then asks for values for each day of the month. It
    stores all those values in a list, the_list and returns it after a value has been entered for every day
    :return: the_list: a list of temperatures for each day
    """
    # initialising an empty list and prompting user for no of days
    days = int(input('How many days in the month?: '))
    the_list = [None] * days
    i = 0

    # looping through for every day and asking the user for the temp
    while i < days:
        temp = int(input('Enter a recorded temperature: '))
        the_list[i] = temp
        i = i + 1

    return the_list


def my_max(the_list):
    """
    This function, given a list of values, will find and return the max value
    :param the_list: a list of integers
    :return: current_max: the max value found in the list or None if the list is empty
    :pre-condition: A list passed into the function only contains numbers
    :post-condition: The function will return the maximum value in the list
    """
    list_length = len(the_list)

    if list_length <= 0:
        return None
    else:
        current_max = the_list[0]

    i = 0
    # loop through the entire list
    while i < list_length:
        # check if the next value if higher then the previous if so, make it the new max
        if current_max < the_list[i]:
            current_max = the_list[i]
        i = i + 1

    return current_max


def my_min(the_list):
    """
    This function, given a list of values, will find and return the min value
    :param the_list: a list of integers
    :return: current_min: the min value found in the list or None if the list is empty
    :pre-condition: A list passed into the function only contains numbers
    :post-condition: The function will return the minimum value in the list
    """
    list_length = len(the_list)
    if list_length <= 0:
        return None
    else:
        current_min = the_list[0]

    i = 0
    # loop through the entire list
    while i < list_length:
        # check if the next value if lower then the previous if so, make it the new min
        if current_min > the_list[i]:
            current_min = the_list[i]
        i = i + 1

    return current_min


def test_max():
    """
    This function uses the created my_max function and compares it to pythons max function. It creates a list of
    random variables and uses both functions.
    :return: An assert if the test fails
    """
    random_vals = []

    # generating 50 random values and appending them to a list
    for i in range(50):
        random_vals.append(random.randrange(0, 1000, 1))

    # using both max functions to find the max
    max_val = my_max(random_vals)
    py_max = max(random_vals)

    assert max_val == py_max, 'Failed on {} - got {}, expected {}'.format(random_vals, max_val, py_max)
    assert my_max([]) is None, 'Failed on {} - got {}, expected {}'.format([], my_max([]), None)
    assert my_max([1]) == 1, 'Failed on {} - got {}, expected {}'.format([1], my_max([1]), 1)


def test_min():
    """
    This function uses the created my_min function and compares it to pythons min function. It creates a list of
    random variables and uses both functions.
    :return: An assert if the test fails
    """
    random_vals = []

    # generating 50 random values and appending them to a list
    for i in range(50):
        random_vals.append(random.randrange(0, 1000, 1))

    # using both max functions to find the max
    min_val = my_min(random_vals)
    py_min = min(random_vals)

    assert min_val == py_min, 'Failed on {} - got {}, expected {}'.format(random_vals, min_val, py_min)
    assert my_min([]) is None, 'Failed on {} - got {}, expected {}'.format([], my_min([]), None)
    assert my_min([1]) == 1, 'Failed on {} - got {}, expected {}'.format([1], my_min([1]), 1)


def main():
    '''
    This function uses the function read_list to get a list of temp from the user. It then uses my_max and my_min to
    find the range between the max value in the list and the min value in the list. It prints the range.
    :return: NA
    '''
    # read the list of numbers
    the_list = read_list()

    # find min and max
    max_temp = my_max(the_list)
    min_temp = my_min(the_list)

    # calculating range and printing
    range = max_temp - min_temp

    print('The range is ' + str(range))


main()




