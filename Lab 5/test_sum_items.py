"""
@author Riley Keane
@since 23/3/18
@modified 28/3/18
"""

import timeit
import random
import matplotlib.pyplot as plt


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


def table_time_sum_items():
    """
    This function runs the sum_items function for random lists of size n = 2 up to n = 4098 where n increases by n^2
    each time. The function records the run time for each list of size n and saves it to a csv file. it also uses
    matplotlib to plot the time taken to generate a list of size n and plot the time taken to sum a list of size n.
    """
    random.seed()
    n = 2
    all_gen_list_times = []
    all_sum_list_times = []
    all_n = []

    # opening csv file and writing column headings
    csv = open("output_ex2.csv", "w")
    csv_row = "n, Time to generate list (ms), Time to sum list (ms)\n"
    csv.write(csv_row)

    while n <= 4098:
        num_list = []
        # starting a timer
        start = timeit.default_timer()

        # generating a list of random numbers of size n
        for i in range(n):
            rand_num = random.random()
            num_list.append(rand_num)
        # recording time taken to create list of size n in ms
        gen_list_time = (timeit.default_timer() - start) * 1000

        # restarting timer
        start = timeit.default_timer()
        # calling the sum_items function to sum random list of size n
        sum_items(num_list)
        # recording time taken to sum list of size n in ms
        sum_list_time = (timeit.default_timer() - start)*1000

        # writing data to csv file
        csv_row = str(n) + ", " + str(gen_list_time) + ", " + str(sum_list_time) + "\n"
        csv.write(csv_row)

        all_n.append(n)
        all_gen_list_times.append(gen_list_time)
        all_sum_list_times.append(sum_list_time)

        # n = n^2
        n = n << 1

    # plotting n vs time to generate a list of random numbers
    gen_list_line, = plt.plot(all_n, all_gen_list_times, label="Time to generate list")
    plt.title("Time to generate list")
    plt.xlabel("n")
    plt.ylabel("Time (ms)")
    # plotting n vs the time taken to run the sum_items function
    sum_list_line, = plt.plot(all_n, all_sum_list_times, label="Time to sum list")
    plt.title("Time to sum list")
    plt.xlabel("n")
    plt.ylabel("Time (ms)")
    plt.legend(handles=[gen_list_line, sum_list_line])
    plt.show()

    csv.close()


table_time_sum_items()



