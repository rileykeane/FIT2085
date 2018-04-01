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
    :complexity: worst case:
    :complexity: best case:
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


def test_shaker_sort():
    for i in range(10):
        random_list = []

        for j in range(10):
            random_val = random.randint(0,30)
            random_list.append(random_val)

        expected = random_list[:]
        expected.sort()
        result = random_list[:]
        shaker_sort(result)

        assert result == expected, 'Failed on {} - got {}, expected {}'.format(random_list, result, expected)

    print("Passed all tests")


def table_time_shaker_sort():
    random.seed()
    n = 2
    all_gen_list_times = []
    all_shaker_sort_times = []
    all_n = []

    csv = open("output_ex3.csv", "w")

    while n <= 1024:
        num_list = []
        start = timeit.default_timer()

        for i in range(n):
            rand_num = random.random()
            num_list.append(rand_num)
        gen_list_time = (timeit.default_timer() - start) * 1000

        start = timeit.default_timer()
        shaker_sort(num_list)
        shaker_sort_time = (timeit.default_timer() - start) * 1000

        csv_row = str(n) + ", " + str(gen_list_time) + ", " + str(shaker_sort_time) + "\n"
        csv.write(csv_row)

        all_n.append(n)
        all_gen_list_times.append(gen_list_time)
        all_shaker_sort_times.append(shaker_sort_time)
        n = n << 1

    csv.close()

    return [all_n, all_gen_list_times, all_shaker_sort_times]


def table_avg_time_shaker_sort():
    random.seed()
    n = 2
    all_gen_list_times = []
    all_avg_shaker_sort_times = []
    all_n = []

    csv = open("output_ex3_avg.csv", "w")

    csv_row = "N, Time to generate 100 lists (ms), Average time to sort list (ms) \n"
    csv.write(csv_row)

    # looping through until n is 1024.
    while n <= 1024:
        sum_shaker_sort_times = 0
        gen_list_time = 0

        # generating 100 lists of random values
        for i in range(100):
            start = timeit.default_timer()
            rand_list = []
            # generating a random list of n numbers
            for j in range(n):
                rand_num = random.random()
                rand_list.append(rand_num)

            gen_list_time += (timeit.default_timer() - start) * 1000

            start = timeit.default_timer()
            shaker_sort(rand_list)
            shaker_sort_time = (timeit.default_timer() - start) * 1000
            sum_shaker_sort_times += shaker_sort_time

        # appending time to generate 100 lists to list with all the times
        all_gen_list_times.append(gen_list_time)

        # calculating average time to sort all 100 random lists
        average_sort_time = sum_shaker_sort_times / 100
        # appending to list with all averages
        all_avg_shaker_sort_times.append(average_sort_time)
        # appending n to all the list with all tge n values
        all_n.append(n)

        csv_row = str(n) + ", " + str(gen_list_time) + ", " + str(average_sort_time) + "\n"
        csv.write(csv_row)

        # n = 2^n
        n = n << 1

    csv.close()

    return [all_n, all_gen_list_times, all_avg_shaker_sort_times]


def plot_table():
    shaker_sort_times = table_time_shaker_sort()
    avg_shaker_sort_times = table_avg_time_shaker_sort()

    shaker_line, = plt.plot(shaker_sort_times[0], shaker_sort_times[2], label='Shaker Sort')
    avg_shaker_line, = plt.plot(avg_shaker_sort_times[0], avg_shaker_sort_times[2], label='Average Shaker Sort')
    plt.legend(handles=[shaker_line, avg_shaker_line])
    plt.xlabel('N')
    plt.ylabel('Time (ms)')
    plt.title('Shaker Sort Times vs Average Shaker Sort Times')
    plt.show()


plot_table()

