class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """
        Push an item onto the stack.
        """
        self.stack.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack. Raises an error if the stack is empty.
        """
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        """
        Return the top item without removing it.
        """
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        """
        Check if the stack is empty.
        """
        return len(self.stack) == 0
