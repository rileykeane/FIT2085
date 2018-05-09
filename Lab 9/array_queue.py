import math


class Queue:
    def __init__(self, size=40):
        self._array = [None]*size
        self._front = 0
        self._rear = 0
        self._count = 0

    def __len__(self):
        return self._count

    def is_empty(self):
        return self._count == 0

    def is_full(self):
        return self._count == len(self._array)

    def append(self, item):
        if self.is_full():
            raise Exception('Queue is full')

        self._array[self._rear] = item
        self._count += 1
        self._rear = (self._rear + 1) % len(self._array)

    def serve(self):
        if self.is_empty():
            raise Exception('Queue is empty')

        item = self._array[self._front]
        self._front = (self._front + 1) % len(self._array)
        return item

