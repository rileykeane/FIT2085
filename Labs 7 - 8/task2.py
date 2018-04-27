import math


class List:
    def __init__(self, size=40, can_resize=True):
        self._length = 0
        self._min_size = size
        self._can_resize = can_resize

        if self._can_resize:
            if self._min_size > 40:
                self._the_array = [None] * self._min_size
            else:
                self._the_array = [None] * 40

    def is_empty(self):
        '''
        Checks if the list is empty return a boolean value
        :return:
        '''
        return self._length == 0

    def is_full(self):
        return self._length == len(self._the_array)

    def unsafe_set_array(self, array, length):
        self._the_array = array
        self._length = length

    def __str__(self):
        list_str = ""

        if self.is_empty():
            return list_str

        for i in range(self._length):
            list_str += str(self._the_array[i]) + '\n'

        return list_str

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        if (index < -1 * len(self)) or (index >= len(self)):
            raise IndexError('Index must be within range of list')

        return self._the_array[index]

    def __setitem__(self, index, item):
        if (index < -1 * len(self)) or (index >= len(self)):
            raise IndexError('Index must be within range of list')

        self._the_array[index] = item

    def __eq__(self, other):
        # returning false if self and other are not the same type or length
        if type(other) is not type(self) or self._length != other._length:
            return False

        for i in range(self._length):
            if self._the_array[i] != other._the_array[i]:
                return False

        return True

    def __contains__(self, item):
        for i in range(self._length):
            if item == self._the_array[i]:
                return True
        return False

    def append(self, item):
        if self.is_full() and not self._can_resize:
            raise Exception('List is full')
        else:
            self.resize()

        self._the_array[self._length] = item
        self._length += 1

    def insert(self, index, item):
        if (index < -1 * len(self)) or (index >= len(self)):
            raise IndexError('Index must be within range of list')

        if self.is_full() and not self._can_resize:
            raise Exception('The list is full')
        else:
            self.resize()

        self._length += 1
        next_item = self._the_array[index + 1]
        self._the_array[index + 1] = self._the_array[index]
        current = next_item
        for i in range(index + 1, self._length - 1):
            next_item = self._the_array[i + 1]
            self._the_array[i + 1] = current
            current = next_item
        self._the_array[index] = item

    def delete(self, index):
        if (index < -1 * len(self)) or (index >= len(self)):
            raise IndexError('Index must be within range of list')

        item = self._the_array[index]
        for i in range(index, self._length - 1):
            self._the_array[i] = self._the_array[i + 1]
        self._length -= 1

        if self._can_resize:
            self.resize()

        return item

    def remove(self, item):
        found = False
        i = 0
        while i < self._length:
            if self._the_array[i] == item:
                found = True
                self.delete(i)
            else:
                i += 1
        if found is not True:
            raise ValueError('Item not in list')

        if self._can_resize:
            self.resize()

    def resize(self):
        array_size = len(self._the_array)

        if self.is_full():
            new_size = math.ceil(self._length * 1.7)
            new_array = [None] * new_size
            for i in range(self._length):
                new_array[i] = self._the_array[i]

            self._the_array = new_array

        if self._length/array_size < 0.25 and array_size > self._min_size:
            new_size = math.ceil(len(self._the_array) / 2)
            if new_size > self._min_size:
                new_array = [None] * new_size
                for i in range(self._length):
                    new_array[i] = self._the_array[i]
                self._the_array = new_array
            else:
                new_array = [None] * self._min_size
                for i in range(self._length):
                    new_array[i] = self._the_array[i]
                self._the_array = new_array
