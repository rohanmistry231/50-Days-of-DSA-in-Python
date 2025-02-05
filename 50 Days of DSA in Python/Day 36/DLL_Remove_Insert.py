class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value, position):
        """
        Insert a node with 'value' at the given 'position' in the DLL.
        """
        new_node = Node(value)
        if position == 0:
            # Insert at the head
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1
        
        if current is None:
            print("Position out of range")
            return
        
        # Insert the new node
        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current

    def remove(self, value):
        """
        Remove the first occurrence of a node with 'value'.
        """
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                return
            current = current.next
        print("Value not found in the list")
