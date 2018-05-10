"""
@author Riley Keane
@since 13/3/18
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


def frequency(item, the_list):
    """
    This function takes a list of integers (the_list) and a single integer (item). It ckecks how many times that
    single integer appears in the list and prints and returns the count.
    the list.
    :param item: A single integer that needs to be checked how many times it is in the list
    :param the_list: A list of integers
    :return: item_count: The number of times item appeared in the list
    :pre-condition: The list inputted into the function must be a list of numbers and the item inputted must also be a
    number that may or may not be in the list
    :post-condition: The function will return how many times the item appears in the list, if it does not appear the
    function will return 0
    """
    list_length = len(the_list)
    # initialising counters
    i = 0
    item_count = 0

    # looping through every item in the list
    while i < list_length:
        # if the item being checked in the list equals the item being searched for, increment the count
        if the_list[i] == item:
            item_count = item_count + 1
        i = i + 1

    # printing the result
    print(str(item) + ' appears ' + str(item_count) + ' times')

    return item_count


def test_frequency():
    """
    This function tests the frequency function. It generates 10 random values and compared the results from the
    frequency function and pythons built in count function. It also tests the frequency function using a selection of
    defined lists
    :return: An assert if the test fails
    """
    random_vals = []

    # generating 50 random integers between 0 and 10 and appending them to a list
    for i in range(50):
        random_vals.append(random.randrange(0, 10, 1))

    # generating 1 random integer to count
    rand_count_val = random.randrange(0, 10, 1)

    # test cases
    tests = [
        (random_vals, rand_count_val, random_vals.count(rand_count_val)),
        ([], 1,  0),
        ([1, 1, 1, 1, 2], 1, 4),
        ([1, 2, 3, 4], 5, 0)
    ]

    # looping through every test case
    for test, item, expected in tests:
        result = frequency(item, test)
        assert result == expected, 'Failed on {} - got {}, expected {}'.format(test, result, expected)


def main():
    """
    This function reads a list of integers from the user using the read_list function, then asks the user for a temop
    and uses the the frequency to find how many times that value appears in the list
    faction to
    :return: NA
    """
    # Reading the list of temps
    the_list = read_list()

    # Getting a temp to count and running frequency function
    count_temp = int(input("Enter a value you would like the frequency of: "))

    # calling the frequency function
    frequency(count_temp, the_list)


# calling the main function
main()





