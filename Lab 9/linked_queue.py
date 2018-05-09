class Node:
    def __init__(self, item=None, link=None):
        self.item = item
        self.link = link


class Queue:
    def __init__(self, _=None):
        self._front = None
        self._rear = None

    def is_empty(self):
        return self._front is None

    def append(self, item):
        new_node = Node(item, None)

        if self.is_empty():
            self._front = new_node
        else:
            self._rear.link = new_node
        self._rear = new_node

    def serve(self):
        if self.is_empty():
            raise Exception('Queue is empty')

        temp = self._front.item
        self._front = self._front.link
        if self._front is None:
            self._rear = None
        return temp



