class Node(object):
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
​
​
class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def push(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            
        
    def pop(self):
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return value
        
    def shift(self):
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return value
​
        
    def unshift(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node