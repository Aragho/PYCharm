class StackOverflowException(Exception):
    pass


class StackUnderFlowException(Exception):
    pass


class Stack:
    def __init__(self):
        self.item_container = [None]
        self.item_size = 0




    def push(self, item):
        if self.item_size == self.item_container:
            raise StackOverflowException("Stack is full")
        self.item_container.insert(self.item_size,item)
        self.item_size += 1

    def peek(self):
        if self.is_empty():
            raise StackUnderFlowException("Stack is empty")
        return self.item_container[self.item_size - 1]

    def is_empty(self):
        return self.item_size == 0

    def pop(self):
        if self.is_empty():
            raise StackUnderFlowException("Stack is empty")
        item = self.item_container[self.item_size - 1]
        self.item_container[self.item_size - 1] = None
        self.item_size -= 1
        return item

    def size(self):
        return self.item_size

    def search(self, item):
        try:
            return self.item_container.index(item) + 1
        except ValueError:
            return -1
