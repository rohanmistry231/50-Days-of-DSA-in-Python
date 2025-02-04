# **Day 47: Binary Trees - Convert Sorted Array to BST & Validate BST**

Welcome to Day 47 of **50 Days of DSA in Python**! Today, we will explore two important binary tree problems: **Convert Sorted Array to BST** and **Validate BST**. These problems focus on constructing and validating binary search trees (BST).

---

### **Topics Covered:**
- Convert Sorted Array to BST
- Validate BST

---

## **1. Convert Sorted Array to BST**

### **Problem Statement**  
Given a sorted array, convert it into a **binary search tree (BST)**. The tree should be height-balanced, meaning that for every node, the difference in heights between the left and right subtrees is at most one.

For example:
- Input: `[-10, -3, 0, 5, 9]`
- Output:  
  ```
        0
       / \
     -3   9
     /   /
   -10  5
  ```

### **Approach**

1. Use the **middle element** of the array as the root to ensure a balanced tree. This ensures that the left and right subtrees have roughly equal nodes.
2. Recursively apply the same logic to the left and right halves of the array.

#### **Code:**
```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sorted_array_to_bst(nums):
    """
    Convert a sorted array to a height-balanced BST.
    """
    if not nums:
        return None
    
    # Find the middle element to be the root
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    
    # Recursively build the left and right subtrees
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])
    
    return root

# Example:
nums = [-10, -3, 0, 5, 9]
root = sorted_array_to_bst(nums)
```

### **Explanation:**
- The middle element of the sorted array is chosen as the root, ensuring that the tree remains balanced.
- The function is called recursively on the left and right halves of the array to build the left and right subtrees.

---

## **2. Validate BST**

### **Problem Statement**  
Given a binary tree, determine if it is a **valid binary search tree (BST)**. For a tree to be a valid BST:
- The left subtree of a node contains only nodes with values **less than** the node’s value.
- The right subtree of a node contains only nodes with values **greater than** the node’s value.
- Both the left and right subtrees must also be valid BSTs.

For example:
- Input:  
  ```
        2
       / \
      1   3
  ```
- Output: `True`

- Input:  
  ```
        5
       / \
      1   4
         / \
        3   6
  ```
- Output: `False` (Because 3 is less than 5 but appears in the right subtree)

### **Approach**

1. Perform a **DFS** traversal of the tree, passing a valid range of values for each node. The value of each node must be between the bounds passed from its parent.
2. At each node, check whether its value is within the range. If not, return `False`.

#### **Code:**
```python
def is_valid_bst(root, low=float('-inf'), high=float('inf')):
    """
    Validate if a binary tree is a valid BST.
    """
    if not root:
        return True
    
    # Check if current node value is within the valid range
    if not (low < root.value < high):
        return False
    
    # Recursively check the left and right subtrees with updated bounds
    return is_valid_bst(root.left, low, root.value) and is_valid_bst(root.right, root.value, high)

# Example:
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print("Is the tree a valid BST?", is_valid_bst(root))  # Output: True
```

### **Explanation:**
- The function uses **recursion** to traverse the tree, checking whether each node’s value lies within the valid range.
- The range is updated as the function traverses down to the left and right children of the tree.
- The left child must be strictly less than the current node, and the right child must be strictly greater.

---

### **Conclusion**

In today’s session, we:
- Implemented the **Convert Sorted Array to BST** algorithm to construct a balanced binary search tree from a sorted array.
- Implemented the **Validate BST** algorithm to verify if a binary tree is a valid binary search tree by checking the ordering property for all nodes.

Key takeaways:
- **Convert Sorted Array to BST** ensures the tree is balanced by selecting the middle element as the root.
- **Validate BST** ensures that the tree satisfies the properties of a binary search tree using a recursive approach with bounds.