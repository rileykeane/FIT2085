import math


class Stack:
    """
    Creates an instance of a stack

    param       size: The size you want the stack to initially be, if left blank its set to 40
    pre         size must be an integer
    complexity  best = worst: O(1)
    """
    def __init__(self, size=40):
        self._min_size = 40
        self._array = [None] * size
        self._top = 0

    def __len__(self):
        """
        The length of the string using len() notation

        return      the length of the stack as an integer
        complexity  best = worst: O(1)
        """
        return self._top

    def __eq__(self, other):
        """
        Finds if two stacks are equal using == notation

        param       other: a stack you want to compare with
        pre         other must be a stack
        complexity  best: O(m) where m is complexity of comparison. If first item in stack is not equal to other
                    worst: O(m*n) where m is complexity of comparison and n is length of the stack
        :return:
        """
        # returning false if self and other are not the same type or length
        if type(other) is not type(self) or self._top != other._top:
            return False

        for i in range(self._top):
            if self._array[i] != other._array[i]:
                return False

        return True

    def is_empty(self):
        """
        returns if the stack is empty or not

        return      True is the stack is empty, false if not
        complexity  best = worst: O(1)
        """
        return self._top == 0

    def is_full(self):
        """
        returns if the stack is full or not

        return      True is the stack is full, false if not
        complexity  best = worst: O(1)
        """
        return self._top == len(self._array)

    def pop(self):
        """
        pops the top item of the stack

        pre         The stack must not be empty
        post        the length will be reduced by one
        post        the top item being poped is no longer valid data
        return      the item from the top of the stack
        complexity  best = worst: O(1)
        """
        if self.is_empty():
            raise Exception('Stack is empty')

        self._top -= 1
        self.resize()
        return self._array[self._top]

    def push(self, item):
        """
        pushes item to the top of the stack

        param       item: the item you want to push onto the stack
        post        the stack will resize if full
        post        the length of the stack will increase by 1
        complexity  best = worst: O(1)
        """
        self.resize()
        self._array[self._top] = item
        self._top += 1

    def resize(self):
        """
        This will resize if the stack is full

        post        if the stack is full it be resize by 1.7 * its length
        post        if the stack is less then 1/4 full the size will reduce by half
        post        length of the stack will remain the same
        post        all elements in the stack will stay the same
        post        the size of the stack will never be less then the size defined at the start
        complexity  best: O(1) if the stack is not full or less then 1/4 empty
        complexity  worst: O(n) if the stack has to increase or decrease
        """
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
        """
        For testing purposes only, allows to you alter the array and top directly

        param       array: the array you want to be set in the stack
        param       top: the index you want top to be at
        pre         top must be an integer
        complexity  best = worst: O(1)
        """
        self._array = array
        self._top = top
