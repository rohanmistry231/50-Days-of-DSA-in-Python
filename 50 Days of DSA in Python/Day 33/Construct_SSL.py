class ListNode:
    def __init__(self, value=0, next=None):
        """
        Initialize a ListNode with a value and a reference to the next node.
        
        Args:
            value (int): The value of the node.
            next (ListNode): The reference to the next node in the list.
        """
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        """
        Initialize an empty Singly Linked List.
        """
        self.head = None

    def append(self, value):
        """
        Append a new node with a given value to the end of the list.
        
        Args:
            value (int): The value to be added to the list.
        """
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """
        Print all the elements of the list.
        """
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
