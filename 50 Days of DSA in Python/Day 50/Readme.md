# **Day 50: Binary Trees - Serialize and Deserialize Binary Tree & N-ary Tree Level Order Traversal**

Congratulations on reaching Day 50 of **50 Days of DSA in Python**! Today, we tackle two advanced problems involving trees: **Serialize and Deserialize Binary Tree** and **N-ary Tree Level Order Traversal**. These problems test your understanding of tree structure serialization, deserialization, and traversal techniques in multi-child trees.

---

### **Topics Covered:**
- Serialize and Deserialize Binary Tree
- N-ary Tree Level Order Traversal

---

## **1. Serialize and Deserialize Binary Tree**

### **Problem Statement**  
The problem involves converting a binary tree to a string (serialization) and converting the string back to the original binary tree (deserialization).

- **Serialization:** Convert the binary tree into a format that can be easily saved or transmitted.
- **Deserialization:** Convert the serialized string back into a binary tree.

For example:
- Input:  
  ```
      1
     / \
    2   3
       / \
      4   5
  ```
- Output (serialized format):  
  `"1,2,#,#,3,4,#,#,5,#,#"`
  - `#` represents a null node in the tree.

### **Approach**

1. **Serialization**:
   - Perform a **pre-order traversal** of the tree.
   - For each node, append its value to the string.
   - If a node is `None`, append a `#` to denote a null node.

2. **Deserialization**:
   - Use the serialized string to rebuild the tree recursively.
   - Split the string by `,` to obtain the values.
   - For each value, if it's a `#`, return `None`. Otherwise, construct the node and recursively process the left and right children.

#### **Code:**
```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        def helper(node):
            if not node:
                return "#"
            return str(node.value) + "," + helper(node.left) + "," + helper(node.right)
        
        return helper(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        values = data.split(",")
        def helper():
            val = values.pop(0)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node
        
        return helper()

# Example:
codec = Codec()
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(5)

serialized = codec.serialize(tree)
print("Serialized:", serialized)  # Output: "1,2,#,#,3,4,#,#,5,#,#"

deserialized = codec.deserialize(serialized)
print("Deserialized root value:", deserialized.value)  # Output: 1
```

### **Explanation:**
- **Serialization:** The `serialize` method converts the tree into a string by performing pre-order traversal.
- **Deserialization:** The `deserialize` method splits the string and recursively constructs the tree.

---

## **2. N-ary Tree Level Order Traversal**

### **Problem Statement**  
Given an **N-ary tree**, return the **level order traversal** (or breadth-first traversal) of its nodes' values.

An N-ary tree is a tree in which each node can have **0 or more children**.

For example:
- Input:  
  ```
  Root
   |
   1
   | \
   2  3
   |
   4
  ```
- Output:  
  ```
  [[1], [2, 3], [4]]
  ```

### **Approach**

1. Perform a **breadth-first traversal** (BFS) using a queue.
2. For each level, visit all the nodes, add their values to the result, and enqueue their children for the next level.

#### **Code:**
```python
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def level_order(root):
    """
    Perform level order traversal on an N-ary tree.
    """
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            queue.extend(node.children)
        result.append(level)
    
    return result

# Example:
root = Node(1)
root.children = [Node(2), Node(3)]
root.children[0].children = [Node(4)]

print("Level Order Traversal:", level_order(root))  # Output: [[1], [2, 3], [4]]
```

### **Explanation:**
- The function `level_order` uses a queue to process each node at a given level.
- For each level, all the nodes are processed and their children are added to the queue for the next iteration.

---

### **Conclusion**

Today, we explored:
- **Serialize and Deserialize Binary Tree**, where we discussed how to convert a binary tree into a string representation and reconstruct it back to the original binary tree using recursion.
- **N-ary Tree Level Order Traversal**, where we performed a breadth-first traversal of an N-ary tree to gather all nodes at each level.

Key takeaways:
- **Serialization and Deserialization** help in saving and transmitting tree structures efficiently.
- **Level Order Traversal** of N-ary trees provides a useful method to visit nodes level by level, especially in hierarchical structures with multiple children per node.