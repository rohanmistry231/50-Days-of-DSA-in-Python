def delete_duplicates(head):
    """
    Remove all duplicate nodes from the linked list.

    Args:
        head (ListNode): The head node of the singly linked list.

    Returns:
        ListNode: The head node after duplicates have been removed.
    """
    current = head
    seen = set()

    while current:
        if current.value in seen:
            # Remove the node by changing the pointer of the previous node
            prev.next = current.next
        else:
            seen.add(current.value)
            prev = current
        current = current.next
    
    return head
