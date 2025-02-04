# **Day 34: Singly Linked Lists**

Welcome to Day 34 of **50 Days of DSA in Python**! Today, we continue our journey with **Singly Linked Lists (SLL)**. We will cover two important operations: **reversing a singly linked list** and **detecting cycles** in the list. These operations are essential for manipulating linked lists and detecting potential issues like infinite loops.

---

### **Topics Covered:**
- Singly Linked Lists  
- Reverse SLL  
- Cycle Detection  

---

## **1. Reverse Singly Linked List (SLL)**

### **Problem Statement**  
Given a singly linked list, reverse the list. After reversing, the head of the list should point to the last element, and the previous elements should point to the next in reverse order.

### **Approach**

#### **1. Iterative Approach to Reverse the List**

To reverse a singly linked list, we need to iterate through the list and reverse the pointers of each node one by one.

#### **Code:**
```python
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
```

---

## **2. Cycle Detection in Singly Linked List**

### **Problem Statement**  
Given a singly linked list, detect if it has a cycle. A cycle occurs when a node’s next pointer points back to a previously visited node, creating a loop in the list.

### **Approach**

#### **1. Floyd’s Tortoise and Hare Algorithm (Cycle Detection)**

Floyd’s Tortoise and Hare algorithm is an efficient way to detect cycles in a linked list. It uses two pointers: one slow (tortoise) and one fast (hare). If there’s a cycle, the fast pointer will eventually meet the slow pointer.

#### **Code:**
```python
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
```

---

### **Conclusion**

Today, we learned how to manipulate **Singly Linked Lists (SLL)** in two important ways:

1. **Reverse Singly Linked List**: We implemented a method to reverse the entire linked list by iteratively adjusting the pointers of each node.

2. **Cycle Detection**: We implemented **Floyd’s Tortoise and Hare algorithm** to detect if a linked list contains a cycle, which is crucial in identifying infinite loops in the list.

Both of these operations are commonly used in various algorithmic problems involving linked lists. By mastering these techniques, you'll be well-prepared for problems requiring linked list manipulations.

Keep practicing, and see you tomorrow for more exciting topics in data structures!