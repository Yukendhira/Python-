class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = Node(value)

    def print_squares(self):
        cur = self.head
        while cur:

