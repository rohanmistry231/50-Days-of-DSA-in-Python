# **Day 44: Binary Trees - Level Order Traversal 2 & Zigzag Traversal**

Welcome to Day 44 of **50 Days of DSA in Python**! In this session, we will continue our exploration of **Level Order Traversal** with a variant called **Level Order Traversal 2**, and we will learn how to perform **Zigzag Traversal** (also known as Spiral Order Traversal) on a binary tree.

---

### **Topics Covered:**
- Level Order Traversal 2
- Zigzag (Spiral) Traversal

---

## **1. Level Order Traversal 2**

### **Problem Statement**  
Given a binary tree, return its **level order traversal**, but the nodes at each level should be **grouped in a list**, maintaining the level order.

For example:
- Input: `[1,2,3,4,5,6,7]`
- Output: `[[1], [2, 3], [4, 5, 6, 7]]`

### **Approach**

1. Use a **queue** for the breadth-first traversal.
2. For each level, traverse the nodes, and add them to the result list corresponding to their level.

#### **Code:**
```python
from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def level_order_traversal_2(root):
    """
    Perform level order traversal where each level's nodes are in a separate list.
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level = []
        level_length = len(queue)
        
        for _ in range(level_length):
            node = queue.popleft()
            level.append(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

# Example:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Level Order Traversal 2:", level_order_traversal_2(root))
```

### **Explanation:**
- In **Level Order Traversal 2**, we process nodes level by level, but instead of printing them directly, we store all nodes at the current level in a list and append that list to the result.
- This ensures that the output is a list of lists, where each inner list contains the nodes at that level.

---

## **2. Zigzag (Spiral) Traversal**

### **Problem Statement**  
Given a binary tree, perform a **Zigzag** (or Spiral) level order traversal. The traversal alternates between left to right and right to left at each level.

For example:
- Input: `[1,2,3,4,5,6,7]`
- Output: `[[1], [3, 2], [4, 5, 6, 7]]`

### **Approach**

1. Use a **deque** to keep track of nodes in the current level.
2. Use a **flag** to toggle between left to right and right to left traversal.
3. For each level, add nodes from left to right or right to left, depending on the flag, and then toggle the flag for the next level.

#### **Code:**
```python
def zigzag_traversal(root):
    """
    Perform a Zigzag (Spiral) level order traversal of a binary tree.
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level = []
        level_length = len(queue)
        
        for _ in range(level_length):
            node = queue.popleft()
            level.append(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # If the current level's traversal is from right to left, reverse the level
        if not left_to_right:
            level.reverse()
        
        result.append(level)
        
        # Toggle the direction for the next level
        left_to_right = not left_to_right
    
    return result

# Example:
print("Zigzag Traversal:", zigzag_traversal(root))
```

### **Explanation:**
- We use a **deque** to perform level order traversal.
- The `left_to_right` flag is used to determine the direction of traversal at each level. If `True`, we process the nodes from left to right; if `False`, we reverse the order before adding the nodes to the result.
- The flag is toggled after each level, ensuring that the direction alternates.

---

### **Conclusion**

In today’s session, we:
- Implemented **Level Order Traversal 2**, where nodes at each level are stored in separate lists.
- Learned how to perform **Zigzag (Spiral) Traversal**, where the nodes at each level alternate in direction.

Key takeaways:
- **Level Order Traversal 2** is a simple extension of level order traversal, where nodes are grouped by their levels.
- **Zigzag Traversal** requires toggling the direction of traversal at each level, which can be done efficiently using a deque and a flag.