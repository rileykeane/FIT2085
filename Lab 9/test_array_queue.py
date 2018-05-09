from array_queue import Queue as ArrayQueue

my_queue = ArrayQueue()
my_queue.append(10)
my_queue.append(12)
my_queue.append(67)

print(my_queue.serve())
print(my_queue.serve())
