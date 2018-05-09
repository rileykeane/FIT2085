import timeit
import matplotlib.pyplot as plt
import gc
from array_stack import Stack as ArrayStack
from linked_stack import Stack as LinkedStack

all_n = []
array_times = []
linked_times = []

array_stack = ArrayStack()
linked_stack = LinkedStack()

for i in range(10000):
    all_n.append(i)

    start = timeit.default_timer()
    linked_stack.push(82)
    linked_push_time = timeit.default_timer() - start
    linked_times.append(linked_push_time)

    start = timeit.default_timer()
    array_stack.push(82)
    array_push_time = timeit.default_timer() - start
    array_times.append(array_push_time)

for i in range(9999):
    linked_stack.pop()
    array_stack.pop()


array_time_line, = plt.plot(all_n, array_times, label="Pushing for array list")
linked_time_line, = plt.plot(all_n, linked_times, label="Pushing for linked list")
plt.xlabel("n")
plt.ylabel("Time (ms)")
plt.legend(handles=[array_time_line, linked_time_line])
plt.show()


