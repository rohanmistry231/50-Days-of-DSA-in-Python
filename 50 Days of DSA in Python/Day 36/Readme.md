# **Day 36: Doubly Linked Lists (DLL)**

Welcome to Day 36 of **50 Days of DSA in Python**! Today, we delve into **Doubly Linked Lists (DLL)**, a more advanced version of singly linked lists. In DLL, each node has pointers to both the next and previous nodes, allowing for more flexible traversal. We will focus on the operations to **remove and insert nodes** and **remove all instances of a value** from a DLL.

---

### **Topics Covered:**
- Doubly Linked Lists  
- DLL Remove Insert  
- DLL Remove All  

---

## **1. Remove Insert in Doubly Linked List**

### **Problem Statement**  
Given a doubly linked list, we need to implement the operations to insert a node at a specified position and remove a node from the list.

### **Approach**

#### **1. Insert and Remove Node in DLL**

To insert a node, we adjust the previous and next pointers of the adjacent nodes. Similarly, for removing a node, we need to update the pointers of the previous and next nodes, taking care to handle edge cases such as removing the head or tail of the list.

#### **Code:**
```python
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
```

---

## **2. Remove All Instances of a Value in Doubly Linked List**

### **Problem Statement**  
Given a doubly linked list, we need to remove **all instances** of a specific value from the list.

### **Approach**

#### **1. Traverse the DLL and Remove Nodes**

We need to iterate through the list and remove all nodes that have the specified value, handling edge cases like removing the head or tail nodes or when the value does not exist.

#### **Code:**
```python
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def remove_all(self, value):
        """
        Remove all nodes with the given 'value' from the DLL.
        """
        current = self.head
        while current:
            next_node = current.next  # Store next node to avoid losing reference
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
            current = next_node
```

---

### **Conclusion**

Today, we worked with **Doubly Linked Lists (DLL)** and implemented two essential operations:

1. **Insert and Remove Node**: We covered the process of inserting and removing nodes at specific positions in a DLL while correctly updating the adjacent pointers.
   
2. **Remove All Instances of a Value**: We implemented an efficient approach to traverse the DLL and remove all nodes containing a specific value, handling edge cases appropriately.

By mastering these operations, you now have the ability to manipulate doubly linked lists effectively, and you're one step closer to solving more complex linked list problems. Keep practicing, and we’ll dive into more exciting topics in the coming days!