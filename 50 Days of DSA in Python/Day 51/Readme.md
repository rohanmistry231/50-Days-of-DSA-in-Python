# **Day 51: Heaps - Max Heap & Min Priority Queue**

Welcome to **Day 51** of the **50 Days of DSA in Python**! In today's session, we'll dive into **Heaps**, specifically covering **Max Heap** and **Min Priority Queue**. These data structures are highly useful in scenarios where we need quick access to the maximum or minimum elements.

---

### **Topics Covered:**
- Max Heap
- Min Priority Queue

---

## **1. Max Heap**

### **Problem Statement**  
A **Max Heap** is a binary tree where the key of each node is greater than or equal to the keys of its children. The largest element is always at the root, making it useful for problems like finding the maximum value efficiently.

### **Properties of Max Heap:**
- The root node contains the largest element.
- The value of each node is greater than or equal to the values of its children.
- The tree is a complete binary tree, meaning all levels are fully filled except possibly the last, which is filled from left to right.

### **Approach to Implement Max Heap:**
- **Insert operation:** Add the element at the end of the tree and "heapify up" to restore the max-heap property.
- **Remove operation (extract max):** Remove the root element, replace it with the last element, and "heapify down" to restore the heap property.

### **Code:**
```python
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0 and self.heap[index] > self.heap[(index - 1) // 2]:
            self.heap[index], self.heap[(index - 1) // 2] = self.heap[(index - 1) // 2], self.heap[index]
            index = (index - 1) // 2

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return max_val

    def _heapify_down(self, index):
        while 2 * index + 1 < len(self.heap):
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2
            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right
            if largest == index:
                break
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

# Example:
heap = MaxHeap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(15)
print("Max value:", heap.extract_max())  # Output: 20
print("Max value:", heap.extract_max())  # Output: 15
```

### **Explanation:**
- **Insert:** Adds the new element at the end and ensures the heap property is maintained by moving the element up if necessary.
- **Extract Max:** Removes the root (maximum value), replaces it with the last element, and restores the heap property by moving the new root down to its correct position.

---

## **2. Min Priority Queue**

### **Problem Statement**  
A **Min Priority Queue** is a special type of priority queue where the smallest element has the highest priority. This is typically implemented using a **Min Heap**, where the smallest element is always at the root.

### **Properties of Min Priority Queue:**
- The root node always contains the smallest element.
- Supports efficient insertions and extractions of the minimum element.
- Often used in algorithms like **Dijkstra's shortest path** and **Huffman coding**.

### **Approach to Implement Min Priority Queue:**
- **Insert operation:** Insert the element into the heap and "heapify up" to ensure the minimum element is at the root.
- **Extract operation (extract min):** Remove the root element and "heapify down" to restore the heap property.

### **Code:**
```python
import heapq

class MinPriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        heapq.heappush(self.heap, val)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        return heapq.heappop(self.heap)

# Example:
pq = MinPriorityQueue()
pq.insert(10)
pq.insert(5)
pq.insert(15)
pq.insert(2)

print("Min value:", pq.extract_min())  # Output: 2
print("Min value:", pq.extract_min())  # Output: 5
```

### **Explanation:**
- **Insert:** The `heapq.heappush` function inserts an element and maintains the min-heap property, ensuring the smallest element is always at the root.
- **Extract Min:** The `heapq.heappop` function extracts the root element (the smallest one) and ensures the heap property is maintained.

---

### **Conclusion**

Today, we learned about:
- **Max Heap**, where the largest element is always at the root, useful for efficient access to the maximum element.
- **Min Priority Queue**, implemented using a Min Heap, where the smallest element is always at the root, ensuring efficient access to the minimum element.

Key takeaways:
- Heaps are efficient data structures for scenarios where we need quick access to the maximum or minimum element.
- **Max Heap** is useful in problems like finding the maximum element or implementing a priority queue with max values.
- **Min Priority Queue**, implemented using a Min Heap, is ideal when we need quick access to the smallest element in a dynamic set of elements.