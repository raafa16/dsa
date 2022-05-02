class Deque:
    def __init__(self):
        self.items = []

    # tests to see whether the deque is empty. It needs no parameters and returns a boolean value.
    def isEmpty(self):
        return self.items == []

    # adds a new item to the front of the deque. It needs the item and returns nothing.
    def addFront(self, item):
        self.items.append(item)

    # adds a new item to the rear of the deque. It needs the item and returns nothing.
    def addRear(self, item):
        self.items.insert(0, item)

    # removes the front item from the deque. It needs no parameters and returns the item. The deque is modified
    def removeFront(self):
        return self.items.pop()

    # removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.
    def removeRear(self):
        return self.items.pop(0)

    # returns the number of items in the deque. It needs no parameters and returns an integer.
    def size(self):
        return len(self.items)
