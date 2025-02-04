Here’s the README for Day 35:

---

# **Day 35: Singly Linked Lists**

Welcome to Day 35 of **50 Days of DSA in Python**! Today, we dive into more advanced **Singly Linked List (SLL)** operations. We will cover two important tasks: **finding duplicates** in a linked list and **adding two numbers represented by linked lists**. These are common problems in linked list manipulations, and mastering them will help you solve many algorithmic challenges.

---

### **Topics Covered:**
- Singly Linked Lists  
- Find Duplicate  
- Add 2 Numbers  

---

## **1. Find Duplicate in Singly Linked List**

### **Problem Statement**  
Given a singly linked list, check if it contains any duplicate values. The list may contain multiple occurrences of the same value, and we need to identify whether this is the case.

### **Approach**

#### **1. Using a Set to Track Seen Elements**

We can use a set to keep track of the values that have already been seen as we traverse the linked list. If we encounter a value that is already in the set, we know there is a duplicate.

#### **Code:**
```python
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
```

---

## **2. Add 2 Numbers Represented by Singly Linked Lists**

### **Problem Statement**  
Given two singly linked lists where each node contains a single digit of a number (in reverse order), add the two numbers and return the sum as a linked list.

### **Approach**

#### **1. Simulate Addition with Carry Over**

We simulate the addition of two numbers digit by digit, starting from the least significant digit. We take care of the carry-over for each digit sum.

#### **Code:**
```python
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
```

---

### **Conclusion**

Today, we explored two important problems related to **Singly Linked Lists (SLL)**:

1. **Find Duplicate**: We used a set to check for duplicate values in a linked list, providing an efficient solution with O(n) time complexity.

2. **Add 2 Numbers**: We simulated the addition of two numbers represented by linked lists, handling carry-overs and constructing the resulting linked list in the process.

By mastering these tasks, you can efficiently manipulate linked lists to solve a wide range of problems. Continue practicing, and stay tuned for more DSA concepts in the next days!

---

Let me know if you need any adjustments or further explanations!