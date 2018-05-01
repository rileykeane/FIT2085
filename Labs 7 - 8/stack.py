import math


class Stack:
    def __init__(self, size=40):
        self._min_size = 40
        self._array = [None] * size
        self._top = 0

    def __len__(self):
        return self._top

    def __eq__(self, other):
        # returning false if self and other are not the same type or length
        if type(other) is not type(self) or self._top != other._top:
            return False

        for i in range(self._top):
            if self._array[i] != other._array[i]:
                return False

        return True

    def is_empty(self):
        return self._top == 0

    def is_full(self):
        return self._top == len(self._array)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')

        self._top -= 1
        self.resize()
        return self._array[self._top]

    def push(self, item):
        self.resize()
        self._array[self._top] = item
        self._top += 1

    def resize(self):
        array_size = len(self._array)

        if self.is_full():
            new_size = int(math.ceil(self._top * 1.7))
            new_array = [None] * new_size
            for i in range(self._top):
                new_array[i] = self._array[i]

            self._array = new_array

        if self._top / array_size < 0.25 and array_size > self._min_size:
            new_size = int(math.ceil(len(self._array) / 2))
            if new_size > self._min_size:
                new_array = [None] * new_size
                for i in range(self._top):
                    new_array[i] = self._array[i]
                self._array = new_array
            else:
                new_array = [None] * self._min_size
                for i in range(self._top):
                    new_array[i] = self._array[i]
                self._array = new_array

    def unsafe_set_stack(self, array, top):
        self._array = array
        self._top = top
