import random
"""
@author Riley Keane
@since 11/3/18
@modified 13/3/18
"""


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
    :return: current_max: the max value found in the list
    """
    current_max = the_list[0]
    list_length = len(the_list)
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
    :return: current_min: the min value found in the list
    """
    current_min = the_list[0]
    list_length = len(the_list)
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
    random variables and uses both functions. If the returns the same value, then the my_max function passes the test
    and true is returned
    :return: true if the test is passed and false if it isn't
    """
    random_vals = []

    # generating 50 random values and appending them to a list
    for i in range(50):
        random_vals.append(random.randrange(0, 1000, 1))

    # using both max functions to find the max
    max_val = my_max(random_vals)
    py_max = max(random_vals)

    # if both functions have the same value return true else return false
    if max_val == py_max:
        return True
    else:
        return False


def test_min():
    """
    This function uses the created my_min function and compares it to pythons min function. It creates a list of
    random variables and uses both functions. If the returns the same value, then the my_min function passes the test
    and true is returned
    :return: true if the test is passed and false if it isn't
    """
    # generating 50 random values and appending them to a list
    random_vals = []

    for i in range(50):
        random_vals.append(random.randrange(0, 1000, 1))

    # using both min functions to find the min
    min_val = my_min(random_vals)
    py_min = min(random_vals)

    # if both functions have the same value return true else return false
    if min_val == py_min:
        return True
    else:
        return False


def main():
    # read the list of numbers
    the_list = read_list()

    # find min and max
    max_temp = my_max(the_list)
    min_temp = my_min(the_list)

    # calculating range and printing
    range = max_temp - min_temp

    print('The range is ' + str(range))


main()



