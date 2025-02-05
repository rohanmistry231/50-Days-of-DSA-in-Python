class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    """
    Add two numbers represented by singly linked lists.

    Args:
        l1 (ListNode): The first input linked list representing a number.
        l2 (ListNode): The second input linked list representing a number.

    Returns:
        ListNode: A new linked list representing the sum of the two numbers.
    """
    carry = 0
    dummy_head = ListNode(0)  # Dummy node to simplify the logic
    current = dummy_head
    
    while l1 or l2 or carry:
        # Extract values from the nodes, or 0 if the node is None
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Add the values and the carry
        total = val1 + val2 + carry
        
        carry = total // 10  # Calculate the new carry
        current.next = ListNode(total % 10)  # Add the digit to the result
        current = current.next
        
        # Move to the next nodes
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    return dummy_head.next  # Return the result without the dummy head
