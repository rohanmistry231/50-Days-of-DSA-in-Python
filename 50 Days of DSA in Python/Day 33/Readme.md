# **Day 33: Singly Linked Lists**

Welcome to Day 33 of **50 Days of DSA in Python**! Today, we will be diving into **Singly Linked Lists (SLL)**. Linked lists are a fundamental data structure used in many algorithmic problems. We'll learn how to construct a singly linked list and how to perform an operation to **delete duplicates** from the list.

---

### **Topics Covered:**
- Singly Linked Lists  
- Construct SLL  
- Delete Duplicates  

---

## **1. Constructing a Singly Linked List (SLL)**

### **Problem Statement**  
A singly linked list (SLL) is a linear data structure where each element (node) points to the next element in the sequence. Each node has two parts: data and a reference (link) to the next node. The last node points to **None**.

### **Approach**

#### **1. Singly Linked List Node Class**

A basic node in a singly linked list will store a value and a reference to the next node. Let's create a class for the node.

#### **Code:**
```python
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
```

---

## **2. Delete Duplicates from Singly Linked List**

### **Problem Statement**  
Given a singly linked list, remove all duplicates such that each element appears only once.

### **Approach**

#### **1. Deleting Duplicates**

To delete duplicates, we can use a set to keep track of the values we've already encountered. As we iterate through the linked list, we remove nodes whose value is already in the set.

#### **Code:**
```python
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
```

---

### **Conclusion**

Today, we covered two important topics related to **Singly Linked Lists**:

1. **Constructing a Singly Linked List**: We learned how to define a node in a singly linked list, append new elements to it, and print the list.

2. **Delete Duplicates from Singly Linked List**: We implemented a method to remove duplicate values from the linked list, ensuring that only unique elements remain in the list.

Singly Linked Lists are a great way to understand how data structures are built and manipulated in memory, and mastering them will be useful in various algorithmic challenges.

Keep practicing, and see you tomorrow for more data structure topics!