def has_duplicate(head):
    """
    Check if the singly linked list contains any duplicates.

    Args:
        head (ListNode): The head node of the singly linked list.

    Returns:
        bool: True if there are duplicates, False otherwise.
    """
    seen = set()
    current = head
    
    while current:
        if current.val in seen:
            return True  # Duplicate found
        seen.add(current.val)
        current = current.next
    
    return False  # No duplicates
