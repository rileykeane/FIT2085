"""
@Author:    Riley Keane
@Created:   04/05/18
@Modified:  04/05/18
"""

import math


class Stack:
    def __init__(self, size=10):
        self._array = [None]*size
        self._top = 0
        self._min_size = size

    def __len__(self):
        return self._top

    def __eq__(self, other):
        if type(self) == type(other) and len(other) == len(self):
            for i in range(len(self)):
                if other._array[i] != self._array[i]:
                    return False
        else:
            return False
        return True

    def __str__(self):
        my_str = ''
        for i in range(len(self)):
            my_str += str(self._array[i]) + ' '

        return my_str

    def is_empty(self):
        return self._top == 0

    def resize(self):
        n = len(self._array)

        # increasing size if full
        if self._top == n:
            new_size = int(math.ceil(n*1.7))
            new_array = [None] * new_size
            for i in range(len(self)):
                new_array[i] = self._array[i]
            self._array = new_array

        # decreasing size if too empty
        if self._top < n/4 and n > self._min_size:
            new_size = int(math.ceil(n/2))
            if new_size > self._min_size:
                new_array = [None] * new_size
            else:
                new_array = [None] * self._min_size
            for i in range(len(self)):
                new_array[i] = self._array[i]
            self._array = new_array

    def push(self, item):
        self.resize()
        self._array[self._top] = item
        self._top += 1

    def pop(self):
        self._top -= 1
        item = self._array[self._top]
        self.resize()
        return item

    def peek(self):
        return self._array[self._top - 1]

    def unsafe_set_array(self, array, top):
        self._array = array
        self._top = top
