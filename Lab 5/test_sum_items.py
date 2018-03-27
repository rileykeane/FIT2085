"""
@author Riley Keane
@since 23/3/18
@modified 23/3/18
"""

import timeit
import random
import matplotlib.pyplot as plt


def sum_items(a_list):
    list_len = len(a_list)

    if list_len <= 0:
        return 0

    list_sum = 0
    for num in a_list:
        list_sum = list_sum + num

    return list_sum


def table_time_sum_items():
    random.seed()
    n = 2
    all_gen_list_times = []
    all_sum_list_times = []
    all_n = []

    csv = open("sum_items_table.csv", "w")

    while n <= 4098:
        num_list = []
        start = timeit.default_timer()

        for i in range(n):
            rand_num = random.random()
            num_list.append(rand_num)
        gen_list_time = timeit.default_timer() - start

        start = timeit.default_timer()
        sum_items(num_list)
        sum_list_time = timeit.default_timer() - start

        csv_row = str(n) + ", " + str(gen_list_time) + ", " + str(sum_list_time) + "\n"
        csv.write(csv_row)

        all_n.append(n)
        all_gen_list_times.append(gen_list_time)
        all_sum_list_times.append(sum_list_time)
        n = n << 1

    # plotting n vs time to generate a list of random numbers
    plt.plot(all_n, all_gen_list_times)
    plt.show()
    # plotting n vs the time taken to run the sum_items function
    plt.plot(all_n, all_sum_list_times)
    plt.show()

    csv.close()


table_time_sum_items()