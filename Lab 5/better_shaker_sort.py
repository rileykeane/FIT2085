"""
@author Riley Keane
@since 27/3/18
@modified 28/3/18
"""
import random
import timeit
import matplotlib.pyplot as plt


def shaker_sort(a_list):
    """
    This function will sort a list of items in ascending order
    :param a_list: a list of sortable items
    :return: the list sorted in ascending order
    :pre-conditions: The list must be of the same type, i.e. the list cannot contain numbers AND stings, it can only
    contain numbers OR strings.
    :post-conditions: The function will return the list sorted in acceding order
    :complexity: worst case: O(n^2)
    :complexity: best case: O(n) for a sorted list
    """
    is_sorted = False
    length = len(a_list)

    while not is_sorted:
        is_sorted = True
        mark_end = length - 1
        mark_start = 0

        for i in range(mark_end):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
                is_sorted = False
        mark_end -= 1

        for i in range(mark_end, mark_start, -1):
            if a_list[i - 1] > a_list[i]:
                temp = a_list[i]
                a_list[i] = a_list[i - 1]
                a_list[i - 1] = temp
                is_sorted = False
        mark_start += 1

    return a_list


def better_shaker_sort(a_list):
    """
    This function will sort a list of items in ascending order
    :param a_list: a list of sortable items
    :return: the list sorted in ascending order
    :pre-conditions: The list must be of the same type, i.e. the list cannot contain numbers AND stings, it can only
    contain numbers OR strings.
    :post-conditions: The function will return the list sorted in acceding order
    :complexity: worst case:
    :complexity: best case:
    """
    is_sorted = False
    length = len(a_list)

    while not is_sorted:
        is_sorted = True
        mark_end = length - 1
        mark_start = 0

        for i in range(mark_start, mark_end, 1):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
                is_sorted = False
                mark_end = i

        for i in range(mark_end, mark_start, -1):
            if a_list[i - 1] > a_list[i]:
                temp = a_list[i]
                a_list[i] = a_list[i - 1]
                a_list[i - 1] = temp
                mark_start = i
                is_sorted = False

    return a_list


def test_sort_func(func):
    for i in range(10):
        random_list = []

        for j in range(100):
            random_val = random.randint(0,30)
            random_list.append(random_val)

        expected = random_list[:]
        expected.sort()
        result = random_list[:]
        func(result)

        assert result == expected, 'Failed on {} - got {}, expected {}'.format(random_list, result, expected)

    print("Passed all tests")


def table_avg_time_shaker_sort():
    random.seed()
    n = 2
    all_avg_shaker_sort_times = []
    all_avg_better_shaker_sort_times = []
    all_n = []

    # looping through until n is 1024.
    while n <= 1024:
        sum_shaker_sort_times = 0
        sum_better_shaker_sort_times = 0

        # generating 100 lists of random values
        for i in range(100):
            rand_list = []
            # generating a random list of n numbers
            for j in range(n):
                rand_num = random.random()
                rand_list.append(rand_num)

            start = timeit.default_timer()
            shaker_sort(rand_list[:])
            shaker_sort_time = (timeit.default_timer() - start) * 1000
            sum_shaker_sort_times += shaker_sort_time

            start = timeit.default_timer()
            better_shaker_sort(rand_list[:])
            better_shaker_sort_time = (timeit.default_timer() - start) * 1000
            sum_better_shaker_sort_times += better_shaker_sort_time

        # calculating average time to sort all 100 random lists
        average_sort_time = sum_shaker_sort_times / 100
        # appending to list with all averages
        all_avg_shaker_sort_times.append(average_sort_time)
        # appending n to all the list with all tge n values

        # calculating average time to sort all 100 random lists
        average_better_sort_time = sum_better_shaker_sort_times / 100
        # appending to list with all averages
        all_avg_better_shaker_sort_times.append(average_better_sort_time)

        # appending n to all the list with all tge n values
        all_n.append(n)

        n = n << 1

    # plotting n vs the average time taken to run the sum_items function 100 times
    shaker_line, = plt.plot(all_n, all_avg_shaker_sort_times, label='Average Shaker Sort Time')
    better_shaker_line, = plt.plot(all_n, all_avg_better_shaker_sort_times, label='Average Better Shaker Sort')
    plt.legend(handles=[shaker_line, better_shaker_line])
    plt.xlabel('N')
    plt.ylabel('Time (ms)')
    plt.title('Shaker Sort VS Better Shaker Sort')
    plt.show()


table_avg_time_shaker_sort()