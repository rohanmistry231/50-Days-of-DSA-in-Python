def reverse_linked_list(head):
    """
    Reverse the given singly linked list.

    Args:
        head (ListNode): The head node of the singly linked list.

    Returns:
        ListNode: The new head node after the list has been reversed.
    """
    prev = None
    current = head
    
    while current:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the current node's pointer
        prev = current            # Move prev and current one step forward
        current = next_node

    return prev  # New head of the reversed list
