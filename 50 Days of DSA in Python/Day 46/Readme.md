# **Day 46: Binary Trees - Invert Tree & Diameter of Tree**

Welcome to Day 46 of **50 Days of DSA in Python**! Today, we will be covering two important binary tree problems: **Invert Tree** and **Diameter of Tree**. These problems focus on tree manipulations and tree-based properties.

---

### **Topics Covered:**
- Invert Tree
- Diameter of Tree

---

## **1. Invert Tree**

### **Problem Statement**  
Given a binary tree, invert it (flip it upside down) and return its root. The inversion process swaps the left and right child nodes of every node in the tree.

For example:
- Input: `[4,2,7,1,3,6,9]`
- Output: `[4,7,2,9,6,3,1]`

### **Approach**

1. **Recursive Approach**: Swap the left and right children of every node in the tree. Recursively call the function on the left and right subtrees.
2. **Iterative Approach**: Use a queue or stack to perform a level-order or DFS traversal and swap the children of each node.

#### **Code (Recursive):**
```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def invert_tree(root):
    """
    Invert a binary tree recursively.
    """
    if not root:
        return None
    
    # Swap the left and right children
    root.left, root.right = root.right, root.left
    
    # Recursively invert the left and right subtrees
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root

# Example:
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

inverted_root = invert_tree(root)
```

### **Explanation:**
- The function swaps the left and right children of the current node and then recursively inverts the left and right subtrees.
- This approach works for both balanced and unbalanced binary trees.

---

## **2. Diameter of Tree**

### **Problem Statement**  
The **diameter** of a binary tree is the length of the longest path between two nodes in the tree. This path may or may not pass through the root. The length of the path is measured in the number of edges.

For example:
- Input: `[1,2,3,4,5]`
- Output: `3` (The longest path is between nodes 4 and 5, and it has 3 edges)

### **Approach**

1. Perform a **Depth-First Search (DFS)** to calculate the height of each node. During the traversal, calculate the diameter by considering the sum of the heights of the left and right subtrees at each node.
2. The **diameter** is the maximum value of the sum of left and right heights for all nodes.

#### **Code:**
```python
def diameter_of_tree(root):
    """
    Calculate the diameter of a binary tree.
    The diameter is the longest path between any two nodes in the tree.
    """
    def helper(node):
        """
        Returns the height of the tree rooted at the given node.
        """
        if not node:
            return 0
        
        # Recursively find the height of left and right subtrees
        left_height = helper(node.left)
        right_height = helper(node.right)
        
        # Update the diameter (longest path seen so far)
        diameter[0] = max(diameter[0], left_height + right_height)
        
        # Return the height of the tree rooted at this node
        return 1 + max(left_height, right_height)
    
    diameter = [0]
    helper(root)
    return diameter[0]

# Example:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Diameter of Tree:", diameter_of_tree(root))
```

### **Explanation:**
- **Helper function**: The `helper` function calculates the height of a subtree while also updating the diameter at each node.
- **Height**: The height of a node is the number of edges on the longest path from that node to a leaf node.
- **Diameter**: As we traverse the tree, we calculate the sum of the heights of the left and right subtrees at each node and update the diameter accordingly.

---

### **Conclusion**

In today’s session, we:
- Implemented the **Invert Tree** algorithm to swap the left and right children of all nodes in the tree.
- Calculated the **Diameter of Tree** by finding the longest path between any two nodes in the tree.

Key takeaways:
- **Invert Tree** involves swapping the left and right children of each node.
- The **Diameter of Tree** is the longest path between two nodes, and it can be found by calculating the sum of the heights of the left and right subtrees at each node.