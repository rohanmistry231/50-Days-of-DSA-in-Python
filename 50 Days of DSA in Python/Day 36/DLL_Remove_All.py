class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def remove_all(self, value):
        """
        Remove all nodes with the given 'value' from the DLL.
        """
        current = self.head
        while current:
            next_node = current.next  # Store next node to avoid losing reference
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
            current = next_node
