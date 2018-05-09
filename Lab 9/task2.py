import timeit
import matplotlib.pyplot as plt
import gc
from array_queue import Queue as ArrayQueue
from linked_queue import Queue as LinkedQueue

all_n = []
array_times = []
linked_times = []

array_queue = ArrayQueue(10000)
linked_queue = LinkedQueue()

for i in range(10000):
    all_n.append(i)

    start = timeit.default_timer()
    linked_queue.append(82)
    linked_push_time = timeit.default_timer() - start
    linked_times.append(linked_push_time)

    start = timeit.default_timer()
    array_queue.append(82)
    array_push_time = timeit.default_timer() - start
    array_times.append(array_push_time)

array_time_line, = plt.plot(all_n, array_times, label="Pushing for array list")
linked_time_line, = plt.plot(all_n, linked_times, label="Pushing for linked list")
plt.xlabel("n")
plt.ylabel("Time (ms)")
plt.legend(handles=[array_time_line, linked_time_line])
plt.show()


