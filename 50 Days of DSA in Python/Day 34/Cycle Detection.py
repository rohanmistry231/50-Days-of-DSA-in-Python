def has_cycle(head):
    """
    Detect if there is a cycle in the given singly linked list.

    Args:
        head (ListNode): The head node of the singly linked list.

    Returns:
        bool: True if there is a cycle, False otherwise.
    """
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next           # Move slow pointer by 1 step
        fast = fast.next.next      # Move fast pointer by 2 steps
        
        if slow == fast:           # Cycle detected
            return True
    
    return False  # No cycle
