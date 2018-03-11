import random
"""
@author Riley Keane
@since 11/3/18
@modified 11/3/18
"""


def read_list():
    the_list = []
    days = int(input('How many days in the month?: '))
    i = 0

    while i < days:
        temp = int(input('Enter a recorded temperature: '))
        the_list.append(temp)
        i = i + 1

    return the_list


def my_max(the_list):
    current_max = the_list[0]
    list_length = len(the_list)
    i = 0

    while i < list_length:
        if current_max < the_list[i]:
            current_max = the_list[i]
        i = i + 1

    return current_max


def my_min(the_list):
    current_min = the_list[0]
    list_length = len(the_list)
    i = 0

    while i < list_length:
        if current_min > the_list[i]:
            current_min = the_list[i]
        i = i + 1

    return current_min


def test_max():
    random_vals = []

    for i in range(50):
        random_vals.append(random.randrange(0, 1000, 1))

    max = my_max(random_vals)
    py_max = max(random_vals)

    if my_max == py_max:
        return True
    else:
        return False


def test_min():



print(test_max())

