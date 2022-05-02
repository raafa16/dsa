class Queue:
    def __init__(self):
        self.items = []

    # tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
    def isEmpty(self):
        return self.items == []

    # adds a new item to the rear of the queue. It needs the item and returns nothing.
    def enqueue(self, item):
        self.items.insert(0, item)

    # removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
    def dequeue(self):
        return self.items.pop()

    # returns the number of items in the queue. It needs no parameters and returns an integer.
    def size(self):
        return len(self.items)
