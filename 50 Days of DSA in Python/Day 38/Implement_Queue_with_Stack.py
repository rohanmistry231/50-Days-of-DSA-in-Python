class QueueWithTwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        """
        Enqueue an item to the queue by pushing it onto stack1.
        """
        self.stack1.append(item)

    def dequeue(self):
        """
        Dequeue an item from the queue by transferring elements from stack1 to stack2, if necessary.
        """
        if not self.stack2:  # If stack2 is empty, transfer elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        if not self.stack2:  # If stack2 is still empty, the queue is empty
            raise IndexError("dequeue from empty queue")
        
        return self.stack2.pop()

    def front(self):
        """
        Return the front item without removing it.
        """
        if not self.stack2:  # If stack2 is empty, transfer elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:  # If stack2 is still empty, the queue is empty
            raise IndexError("front from empty queue")
        
        return self.stack2[-1]

    def is_empty(self):
        """
        Check if the queue is empty.
        """
        return not self.stack1 and not self.stack2
