class List:
    def __init__(self, size=40):
        self._length = 0
        self._the_array = [None]*size

    def is_empty(self):
        """
        Checks if the list is empty

        return      A boolean value, true if the list is empty, else false
        complexity  best = worst: O(1)
        """
        return self._length == 0

    def is_full(self):
        """
        Checks if the list is full

        return     A boolean value, true if the list is full, else false
        complexity best = worst: O(1)
        """
        return self._length == len(self._the_array)

    def unsafe_set_array(self, array, length):
        """
        This allows you set the array and length of the list directly
        *MUST ONLY BE USED FOR TESTING*

        param       array: A python list of what the array in List will be set to
        param       length: The number of valid items in array
        pre         the array must be a python list
        pre         length must be an integer value
        pre         the length must be equal to the number of valid items in array
        post        the List will contain the items specified in the param array
        post        the length of the List will be the length specified in the param length
        complexity  best = worst: O(1)
        """
        self._the_array = array
        self._length = length

    def __str__(self):
        """
        Converts the List to a string

        return      a string type containing every valid item in the list
        pre         the list must be defined
        post        each item in the list will be on a new line
        post        only valid data in array will be printed
        complexity  best = worst: O(n) where n is the length of the List
        """
        list_str = ""

        # checking list is not empty
        if self.is_empty():
            return list_str

        # looping through every valid item in the array
        for i in range(self._length):
            list_str += str(self._the_array[i]) + '\n'

        return list_str

    def __len__(self):
        """
        Returns the length of the list

        return      an integer value, the number of valid items in the list
        pre         the list must be defined
        post        the length will be equal to the number of valid items in the list
        complexity  best = worst: O(1)
        :return:
        """
        return self._length

    def __getitem__(self, index):
        """
        Returns the item in the specified index by calling List[index]

        param       index: the index of the item in the List you want returned
        return      the item in the list at the specified index
        pre         index must be an integer between 0 and the length of the list
        post        the list is not altered in any way
        complexity  best = worst: O(1)
        """
        # checking index is valid
        if (index < 0) or (index >= len(self)):
            raise IndexError('Index must be within range of list')

        return self._the_array[index]

    def __setitem__(self, index, item):
        """
        Changes an item in a specified index

        param       index: the index at which you want to change the item
        param       item: the item you want to put it an the position index
        return      NA
        pre         the index must be within 0 and length - 1
        pre         index is 0 for the first item in the list
        post        All items in the list except at index will remain in the same position
        post        The previous item in the index will be overwritten
        complexity  best = worst: O(1)
        """
        if (index < 0) or (index >= len(self)):
            raise IndexError('Index must be within range of list')

        self._the_array[index] = item

    def __eq__(self, other):
        """
        Checks if another List is equivalent

        param       self: A list you want to compare with
        return      True if the lists are equal or false is they are not
        pre         self must be an instance created with the List class
        post        only valid data, that is data in the array from 0 to length - 1 will be compared
        """
        # returning false if self and other are not the same type or length
        if type(other) is not type(self) or self._length != other._length:
            return False

        for i in range(self._length):
            if self._the_array[i] != other._the_array[i]:
                return False

        return True

    def __contains__(self, item):
        """
        Checks if an item exists within a list using python notation, 'if item in list'

        parm        item: the item that you are looking for in the list
        return      true if item in in the list else, false
        complexity  best: O(1) if the item is the first element in the list
        complexity  worst: O(n) where n is the length of the list and occurs when item in not in the list
        """
        for i in range(self._length):
            if item == self._the_array[i]:
                return True
        return False

    def append(self, item):
        if self.is_full():
            raise Exception('List is full')

        self._the_array[self._length] = item
        self._length += 1

    def insert(self, index, item):
        if (index < -1 * len(self)) or (index >= len(self)):
            raise IndexError('Index must be within range of list')

        if self.is_full():
            raise Exception('The list is full')

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
