"""
@author Riley Keane
@since 13/3/18
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


def frequency(item, the_list):
    """
    This function takes a list of integers (the_list) and a single integer (item). It ckecks how many times that
    single integer appears in the list and returns the count.
    the list.
    :param item: A single integer that needs to be checked how many times it is in the list
    :param the_list: A list of integers
    :return: item_count: The number of times item appeared in the list
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

    return item_count


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


def main():
    # reading the list of temps
    the_list = read_list()
    # sorting the list of temps
    bubble_sort(the_list)

    list_length = len(the_list)
    i = 0

    # looping through the length of the list
    while i < list_length:
        item = the_list[i]
        # finding the frequency of each different integer in the list
        freq_count = frequency(item, the_list)
        # printing the result
        print(str(item) + ' appears ' + str(freq_count) + ' times')
        # incrementing i by the number of times the integer appeared in the list
        i = i + freq_count


main()



