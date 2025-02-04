# **Day 38: Queues**

Welcome to Day 38 of **50 Days of DSA in Python**! Today, we explore **Queues**, a fundamental data structure that follows the **First In, First Out (FIFO)** principle. We will cover the **construction of a queue** and how to **implement a queue using stacks**. Queues are essential in situations where the order of processing must follow a specific sequence, such as task scheduling, data buffers, and breadth-first search (BFS).

---

### **Topics Covered:**
- Queues  
- Construct Queue  
- Implement Queue with Stack  

---

## **1. Constructing a Queue**

### **Problem Statement**  
A queue is a linear data structure where elements are added to the **rear** and removed from the **front**. The basic operations of a queue are:
- **enqueue**: Add an element to the rear of the queue
- **dequeue**: Remove the front element
- **front**: View the front element without removing it
- **is_empty**: Check if the queue is empty

### **Approach**

#### **1. Implementing Queue Using Python List**

In Python, a queue can be implemented using a list. We use the `append` method to enqueue elements and the `pop(0)` method to dequeue elements. While this approach works, it is not efficient because removing elements from the front of the list takes O(n) time.

#### **Code:**
```python
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """
        Add an item to the rear of the queue.
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Remove and return the front item from the queue. Raises an error if the queue is empty.
        """
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("dequeue from empty queue")

    def front(self):
        """
        Return the front item without removing it.
        """
        if not self.is_empty():
            return self.queue[0]
        raise IndexError("front from empty queue")

    def is_empty(self):
        """
        Check if the queue is empty.
        """
        return len(self.queue) == 0
```

---

## **2. Implementing Queue with Stack**

### **Problem Statement**  
In this problem, we will implement a queue using two stacks. The goal is to simulate the behavior of a queue while using two stacks to store the elements. The two stacks will help us manage the order of elements such that:
- The first stack (`stack1`) is used for enqueue operations.
- The second stack (`stack2`) is used for dequeue operations.

When we dequeue, if the second stack is empty, we transfer all elements from `stack1` to `stack2` (reversing their order), then pop from `stack2`.

### **Approach**

#### **1. Implementing Queue with Two Stacks**

We will create a class with two stacks. The `enqueue` operation will push elements onto `stack1`, and the `dequeue` operation will pop elements from `stack2`, transferring elements from `stack1` if necessary.

#### **Code:**
```python
class QueueWithTwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        """
        Enqueue an item to the queue by pushing it onto stack1.
        """
        self.stack1.append(item)

    def dequeue(self):
        """
        Dequeue an item from the queue by transferring elements from stack1 to stack2, if necessary.
        """
        if not self.stack2:  # If stack2 is empty, transfer elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        if not self.stack2:  # If stack2 is still empty, the queue is empty
            raise IndexError("dequeue from empty queue")
        
        return self.stack2.pop()

    def front(self):
        """
        Return the front item without removing it.
        """
        if not self.stack2:  # If stack2 is empty, transfer elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:  # If stack2 is still empty, the queue is empty
            raise IndexError("front from empty queue")
        
        return self.stack2[-1]

    def is_empty(self):
        """
        Check if the queue is empty.
        """
        return not self.stack1 and not self.stack2
```

### **Example:**

```python
queue = QueueWithTwoStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Output: 1
print(queue.front())    # Output: 2
queue.enqueue(4)
print(queue.dequeue())  # Output: 2
```

---

### **Conclusion**

Today, we explored **Queues** and applied them to two important problems:

1. **Constructing a Queue**: We implemented a queue using a list and defined basic operations like `enqueue`, `dequeue`, `front`, and `is_empty`.
   
2. **Implementing Queue with Two Stacks**: We simulated a queue using two stacks to efficiently perform enqueue and dequeue operations while maintaining the FIFO order.

By mastering these queue operations, you'll be equipped to handle problems like task scheduling, breadth-first search, and more. Keep practicing, and we’ll continue to explore more data structures and algorithms in the upcoming days!