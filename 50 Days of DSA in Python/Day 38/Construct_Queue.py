class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """
        Add an item to the rear of the queue.
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Remove and return the front item from the queue. Raises an error if the queue is empty.
        """
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("dequeue from empty queue")

    def front(self):
        """
        Return the front item without removing it.
        """
        if not self.is_empty():
            return self.queue[0]
        raise IndexError("front from empty queue")

    def is_empty(self):
        """
        Check if the queue is empty.
        """
        return len(self.queue) == 0
