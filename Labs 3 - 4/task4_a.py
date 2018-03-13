import random
"""
@author Riley Keane
@since 13/3/18
@modified 13/3/18
"""

def bubble_sort(the_list):
    """
    This function uses the bubble sort algorithm to sort a list (the_list) and returns the list in ascending order
    :param the_list: A list of integers
    :return: The same list of integers, sorted in acceding order
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
    bubble sort function and pythons built in sort function. It then checks both methods get the same result
    :return: if the test passes return true, else return false
    """
    random_vals = []

    # generating 50 random integers between 0 and 100 and appending them to a list
    for i in range(50):
        random_vals.append(random.randrange(0, 100, 1))

    # Creating copies of the random values list
    py_sort = random_vals[:]
    my_sort = random_vals[:]

    # sorting copies using bubble sort and pythons built in method
    bubble_sort(my_sort)
    py_sort.sort()

    # Checking if both sorted lists are the same
    if my_sort == py_sort:
        return True
    else:
        return False




