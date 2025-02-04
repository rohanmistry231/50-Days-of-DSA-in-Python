# **Day 45: Binary Trees - Vertical Order Traversal & Sum Root to Leaf Numbers**

Welcome to Day 45 of **50 Days of DSA in Python**! Today, we will be covering two important binary tree traversal techniques: **Vertical Order Traversal** and **Sum Root to Leaf Numbers**. These concepts focus on organizing nodes in specific ways and performing calculations based on tree structure.

---

### **Topics Covered:**
- Vertical Order Traversal
- Sum Root to Leaf Numbers

---

## **1. Vertical Order Traversal**

### **Problem Statement**  
Given a binary tree, return the vertical order traversal of its nodes. The vertical order traversal is defined by the following steps:
1. The nodes in the same vertical line are grouped together.
2. Nodes are sorted from top to bottom and left to right within the same vertical line.

For example:
- Input: `[3,9,20,null,null,15,7]`
- Output: `[[9], [3, 15], [20], [7]]`

### **Approach**

1. Perform a **level order traversal** while keeping track of the **horizontal distance** of each node from the root.
2. Use a **map** (or dictionary) where the key is the horizontal distance, and the value is a list of nodes at that horizontal distance.
3. Sort the keys (horizontal distances) and collect the nodes for each vertical line in order.

#### **Code:**
```python
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def vertical_order_traversal(root):
    """
    Perform vertical order traversal of a binary tree.
    """
    if not root:
        return []

    # A dictionary to hold nodes at each horizontal distance
    column_map = defaultdict(list)
    
    # Queue for level order traversal with horizontal distance
    queue = deque([(root, 0)])  # (node, horizontal_distance)
    
    while queue:
        node, hd = queue.popleft()
        column_map[hd].append(node.value)
        
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    
    # Sort the keys (horizontal distances) and prepare the result
    sorted_columns = sorted(column_map.keys())
    result = [column_map[hd] for hd in sorted_columns]
    
    return result

# Example:
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print("Vertical Order Traversal:", vertical_order_traversal(root))
```

### **Explanation:**
- **Horizontal distance (HD)**: We assign each node a horizontal distance relative to the root. The root starts at HD = 0, the left child has HD = -1, and the right child has HD = +1.
- We store nodes at each horizontal distance in a dictionary (`column_map`).
- After processing all nodes, we sort the dictionary by HD to return the vertical order traversal.

---

## **2. Sum Root to Leaf Numbers**

### **Problem Statement**  
Given a binary tree, each node contains a digit (0-9). Starting from the root, each path down to a leaf node represents a number formed by concatenating the digits along the path. Return the sum of all such numbers.

For example:
- Input: `[1,2,3]`
- Output: `25` (The numbers are 12 and 13, so the sum is 12 + 13 = 25)

### **Approach**

1. Perform a **depth-first traversal (DFS)** starting from the root.
2. For each node, accumulate the number formed by the digits from the root to the current node.
3. If a node is a leaf, add the current number to the result.

#### **Code:**
```python
def sum_root_to_leaf(root, current_sum=0):
    """
    Calculate the sum of all numbers formed from root to leaf.
    """
    if not root:
        return 0
    
    # Update the current sum by appending the current node's value
    current_sum = current_sum * 10 + root.value
    
    # If the node is a leaf, return the current sum
    if not root.left and not root.right:
        return current_sum
    
    # Recursively calculate the sum for the left and right subtrees
    return sum_root_to_leaf(root.left, current_sum) + sum_root_to_leaf(root.right, current_sum)

# Example:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print("Sum Root to Leaf Numbers:", sum_root_to_leaf(root))
```

### **Explanation:**
- **DFS** is used to traverse the tree, with `current_sum` accumulating the digits as we move down the tree.
- When a leaf node is reached, we add the accumulated number to the result.
- The function performs a depth-first traversal recursively, calculating the sum of numbers formed by root-to-leaf paths.

---

### **Conclusion**

In today’s session, we:
- Implemented **Vertical Order Traversal** to group and order nodes based on their vertical position.
- Calculated the **Sum of Root to Leaf Numbers** by recursively traversing the tree and forming numbers from root to leaf paths.

Key takeaways:
- **Vertical Order Traversal** helps to organize nodes by their horizontal distance from the root.
- **Sum Root to Leaf Numbers** allows us to calculate the sum of numbers formed by root-to-leaf paths in a binary tree.