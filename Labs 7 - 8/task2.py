import math


class List:
    def __init__(self, size=40, can_resize=True):
        """
        Creates and instance of list

        param       size: The initial size of the array, set to 40 if left blank
        param       can_resize: A boolean value stating if the array can resize or not. set to True if left blank
        pre         size must be an integer
        pre         can_resize must be a boolean
        post        The list will always have a minimum size of 40 even if you declare it will a size less than
        complexity  best = worst: O(1)
        """

        if type(size) is not int:
            raise ValueError('Size must be an integer')

        self._length = 0
        self._min_size = size
        self._can_resize = can_resize

        if self._can_resize:
            if self._min_size > 40:
                self._the_array = [None] * self._min_size
            else:
                self._the_array = [None] * 40

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
        if (index < -1 * len(self)) or (index >= len(self)):
            raise IndexError('Index must be within range of list')

        if index < 0:
            index = index + self._length

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
        if (index < -1 * len(self)) or (index >= len(self)):
            raise IndexError('Index must be within range of list')

        if index < 0:
            index = index + self._length

        self._the_array[index] = item

    def __eq__(self, other):
        """
        Checks if another List is equivalent

        param       self: A list you want to compare with
        return      True if the lists are equal or false is they are not
        pre         self must be an instance created with the List class
        post        only valid data, that is data in the array from 0 to length - 1 will be compared
        complexity  best: O(m) where m is the complexity of comparison. If the first item in the arrays are not equal
        complexity  worst: O(m*n) where m in complexity of comparison and n is length of the list. If arrays are equal
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
        complexity  best: O(m) where m is complexity of comparison. If the item is the first element in the list
        complexity  worst: O(n*m) where n is the length of the list and m is complexity of comparison and occurs when
                    item in not in the list
        """
        for i in range(self._length):
            if item == self._the_array[i]:
                return True
        return False

    def append(self, item):
        """
        Adds item to the end of the list

        param       item: the item to be added to the end of the list
        pre         If not resizable, list must not be full
        post        If resizeable, the list will resize if full
        post        everything before the appended item will remain in same position
        complexity  best: O(1) if the list does not have to resize
        complexity  worst: O(n) where n is the length of the list. When the list is full and must resize
        """
        # if the list cannot resize, check its not full
        if self.is_full() and not self._can_resize:
            raise Exception('List is full')
        else:
            # if the list can resize, resize if its full
            self.resize()

        # adding element to the end
        self._the_array[self._length] = item
        self._length += 1

    def insert(self, index, item):
        """
        Inserts an item in the specified index

        param       index: the index in you want to item to be in
        param       item: what you are adding to the list
        pre         index must be an integer and within range
        pre         if list is not resizable, it must not be full
        post        every item to the at index - length - 1 will be shifted to the right
        post        all items before index will remain in the same place
        post        if the list is reliable and full, it will resize
        complexity  best: O(1) if the list does not have to resize and inserting at the end
        complexity  worst: O(n) where n is the length of the list. If the list has to resize and inserting at the start
        """
        if (index < -1 * len(self)) or (index >= len(self)):
            raise IndexError('Index must be within range of list')

        if self.is_full() and not self._can_resize:
            raise Exception('The list is full')
        else:
            self.resize()

        if index < 0:
            index = index + self._length

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
        """
        Deletes the item at the specified index

        param       index: the index at which the item is you want to delete
        pre         index must be within range
        pre         index must be an integer
        pre         the list must not be empty
        post        if list is reliable, it will shrink if length is less then 1/4 size after deletion
        post        everything to the right of index will shift one position to the left
        complexity  best: O(1) if deleting index at the end and list does not have to resize
        complexity  worst: O(n) if deleting index from the start and the list has to resize
        """

        if not self._can_resize and self.is_empty():
            raise Exception('The list is empty')

        if (index < -1 * len(self)) or (index >= len(self)):
            raise IndexError('Index must be within range of list')

        if index < 0:
            index = index + self._length

        item = self._the_array[index]
        for i in range(index, self._length - 1):
            self._the_array[i] = self._the_array[i + 1]
        self._length -= 1

        if self._can_resize:
            self.resize()

        return item

    def remove(self, item):
        """
        Removes a specified item from the list

        param       item: the item you want to remove from the list
        post        if list is reliable, it will shrink if length is less then 1/4 size after deletion
        post        everything to the right of index will shift one position to the left
        complexity  best: O(m) where m is the complexity of the comparison if deleting item at the end and list does
                    not have to resize
        complexity  worst: O(n*m) where m is the complexity of the comparison and n is the length of the list. If item
                    is not in the list. and the list has to resize
        """
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
        """
        Re sizes the array by when is full or too empty

        pre         the list must be defined
        pre         resizable must be true
        post        if the list is full it be resize by 1.7 * its length
        post        if the list is less then 1/4 full the size will reduce by half
        post        length of the list will remain the same
        post        all elements in the list will stay the same
        post        the size of the list will never be less then the size defined at the start
        complexity  best: O(1) if the list is not full or less then 1/4 empty
        complexity  worst: O(n) if the list has to increase or decrease
        """
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
