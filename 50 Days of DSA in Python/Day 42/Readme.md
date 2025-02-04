# **Day 42: Construct Binary Tree from Pre and In-order Traversal & In and Post-order Traversal**

Welcome to Day 42 of **50 Days of DSA in Python**! Today, we will explore how to construct a binary tree from its **pre-order** and **in-order** traversals and also learn how to compute the **in-order** and **post-order** traversals of a tree.

---

### **Topics Covered:**
- Construct Binary Tree from Pre-order and In-order Traversal
- In-order and Post-order Traversal

---

## **1. Construct Binary Tree from Pre-order and In-order Traversal**

### **Problem Statement**  
Given the **pre-order** and **in-order** traversals of a binary tree, reconstruct the binary tree.  
- **Pre-order traversal**: Visit the root node, traverse the left subtree, and then traverse the right subtree.
- **In-order traversal**: Traverse the left subtree, visit the root node, and then traverse the right subtree.

The challenge is to use the information from both traversals to rebuild the original binary tree.

### **Approach**

1. **Pre-order traversal** provides the root of the tree first, and using this root, we can split the **in-order traversal** into two parts: the left subtree and the right subtree.
2. Recursively construct the left and right subtrees by using the split parts from the **in-order** traversal and the next elements from the **pre-order** traversal.

#### **Code:**
```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_tree(preorder, inorder):
    """
    Constructs a binary tree from pre-order and in-order traversal lists.
    """
    def helper(preorder, inorder):
        if not preorder or not inorder:
            return None
        
        # The first element of preorder is the root
        root_value = preorder[0]
        root = TreeNode(root_value)
        
        # Find the root in inorder to split left and right subtrees
        root_index = inorder.index(root_value)
        
        # Recursively build the left and right subtrees
        root.left = helper(preorder[1:1 + root_index], inorder[:root_index])
        root.right = helper(preorder[1 + root_index:], inorder[root_index + 1:])
        
        return root
    
    return helper(preorder, inorder)

# Example:
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

root = build_tree(preorder, inorder)
```

### **Explanation:**
- We start by identifying the **root node** from the first element of the **pre-order** list.
- We find this root node in the **in-order** list to determine which nodes belong to the left and right subtrees.
- Then, we recursively build the left and right subtrees by passing the appropriate sections of the **pre-order** and **in-order** lists.

---

## **2. In-order and Post-order Traversal**

### **Problem Statement**  
Given a binary tree, return its **in-order** and **post-order** traversals.  
- **In-order traversal**: Traverse the left subtree, visit the root, and then traverse the right subtree.
- **Post-order traversal**: Traverse the left subtree, traverse the right subtree, and then visit the root.

### **Approach**

For both **in-order** and **post-order** traversals, we can use **recursion** to traverse the left and right subtrees in the specified order:
1. **In-order traversal**: Start by recursively visiting the left subtree, then visit the node, and finally, recursively visit the right subtree.
2. **Post-order traversal**: Start by recursively visiting the left subtree, then the right subtree, and finally, visit the node after both subtrees have been processed.

#### **Code:**
```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def inorder_traversal(self):
        """
        In-order Traversal (Left → Root → Right)
        """
        result = []
        if self.left:
            result.extend(self.left.inorder_traversal())
        result.append(self.value)
        if self.right:
            result.extend(self.right.inorder_traversal())
        return result

    def postorder_traversal(self):
        """
        Post-order Traversal (Left → Right → Root)
        """
        result = []
        if self.left:
            result.extend(self.left.postorder_traversal())
        if self.right:
            result.extend(self.right.postorder_traversal())
        result.append(self.value)
        return result
```

### **Example:**
```python
# Constructing a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# In-order traversal: Left → Root → Right
print("In-order Traversal:", root.inorder_traversal())  
# Output: [4, 2, 5, 1, 3]

# Post-order traversal: Left → Right → Root
print("Post-order Traversal:", root.postorder_traversal())  
# Output: [4, 5, 2, 3, 1]
```

---

### **Conclusion**

In today’s session, we:
- Learned how to **construct a binary tree** from its **pre-order** and **in-order** traversals using recursive logic.
- Explored the **in-order** and **post-order** traversal techniques for binary trees and implemented them recursively.

Key takeaways:
- **Pre-order and In-order traversals** help in uniquely reconstructing a binary tree, with the root found in the pre-order list and the left and right subtrees determined from the in-order list.
- **In-order and Post-order traversals** are foundational techniques in binary tree traversal, and we can easily implement them recursively to explore a tree.