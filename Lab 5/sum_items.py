"""
@author Riley Keane
@since 23/3/18
@modified 28/3/18
"""


def sum_items(a_list):
    """
    This function takes a list of numbers and sums all the numbers in the list
    :param a_list: A list of numbers
    :return: The sum of all numbers in the inputted list
    :pre-condition: The inputted list must contain only numbers
    :post-condition: The function will output a number which is the list sum
    :complexity: Worst Case: O(n) where n is the length of the list
    """
    list_len = len(a_list)

    # if the list is empty return 0
    if list_len <= 0:
        return 0

    # looping through the list and adding each element together
    list_sum = 0
    for num in a_list:
        list_sum += + num

    return list_sum


def test_sum_items():
    """
    This function tests the sum_items function by testing it with a selection of pre defined cases. If the function
    fails the test, it asserts an error otherwise it prints all tests passed
    """
    tests = [
        ([1, 2, 3, 4, 5], 15),
        ([7, 4, 12, 9, 13], 45),
        ([10], 10),
        ([], 0)
    ]

    # running each test and comparing function output to the correct output
    for test, exp_result in tests:
        func_result = sum_items(test)
        assert func_result == exp_result, 'Failed on {} - got {}, expected {}'.format(test, func_result, exp_result)

    print('All tests passed')


test_sum_items()

