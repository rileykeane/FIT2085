"""
@Author:    Riley Keane
@Created:   04/05/18
@Modified:  04/05/18
"""


class Node:
    def __init__(self, item=None, link=None):
        self._item = item
        self._link = link


class Stack:
    def __init__(self, _=None):
        self._top = None

    def __len__(self):
        current = self._top
        length = 0
        while current is not None:
            length += 1
            current = current._link
        return length

    def __str__(self):
        current = self._top
        out_str = ""
        while current is not None:
            out_str += str(current._item) + " "
            current = current._link
        # removing last space
        if len(out_str) > 0:
            out_str = out_str[:-1]
        return out_str

    def __eq__(self, other):
        if type(other) == type(self) and len(other) == len(self):
            self_current = self._top
            other_current = other._top
            while self_current is not None:
                if self_current._item != other_current._item:
                    return False
                else:
                    self_current = self_current._link
                    other_current = other_current._link
        else:
            return False
        return True

    def is_empty(self):
        return self._top is None

    def push(self, item):
        self._top = Node(item, self._top)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')

        item = self._top._item
        self._top = self._top._link
        return item

    def peek(self):
        return self._top._item



