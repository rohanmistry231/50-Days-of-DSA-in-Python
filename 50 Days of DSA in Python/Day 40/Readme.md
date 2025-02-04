# **Day 40: Pre-order and In-order Traversal of Binary Tree - Iterative**

Welcome to Day 40 of **50 Days of DSA in Python**! Today, we focus on performing **Pre-order** and **In-order** tree traversals using **iterative** methods. While recursive approaches are straightforward, iterative solutions offer better control over stack space and can be more efficient in certain scenarios, especially when working with large trees.

---

### **Topics Covered:**
- Pre-order Traversal (Iterative)  
- In-order Traversal (Iterative)  

---

## **1. Iterative Pre-order Traversal**

### **Problem Statement**  
In Pre-order traversal, we visit the **node** first, then recursively visit the **left subtree**, followed by the **right subtree**. Typically implemented using recursion, we will now explore how to implement Pre-order traversal iteratively using an explicit stack.

### **Approach**

We can simulate the recursive calls using an explicit stack:
1. Push the root node onto the stack.
2. While the stack is not empty:
   - Pop the node from the stack and process it.
   - Push the right child (if it exists) onto the stack.
   - Push the left child (if it exists) onto the stack.

This order ensures the node is processed before its children, and the left subtree is processed before the right subtree.

#### **Code:**
```python
class BinaryTree:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

    def iterative_preorder(self):
        """
        Iterative Pre-order Traversal: Node → Left → Right
        """
        if not self:
            return []

        stack = [self]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.value)

            # Push right first, so left is processed first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result
```

### **Example:**
```python
# Constructing the binary tree
root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

print("Iterative Pre-order Traversal:", root.iterative_preorder())  
# Output: [1, 2, 4, 5, 3, 6, 7]
```

---

## **2. Iterative In-order Traversal**

### **Problem Statement**  
In In-order traversal, we recursively visit the **left subtree**, process the **node**, and then recursively visit the **right subtree**. For an iterative solution, we use a stack to simulate the recursive call stack:
1. Push all the left children of the current node onto the stack.
2. When there are no more left children, pop the node from the stack and process it.
3. Move to the right child of the node and repeat the process.

This traversal ensures the nodes are processed in increasing order for a Binary Search Tree (BST).

### **Approach**

The iterative version of In-order traversal requires us to manage the stack and visit nodes from left to right:
1. Push all left children of the current node onto the stack.
2. Once we reach a leaf (or a node with no left child), pop a node from the stack, process it, and then move to its right child.
3. Repeat the process for the right child.

#### **Code:**
```python
class BinaryTree:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

    def iterative_inorder(self):
        """
        Iterative In-order Traversal: Left → Node → Right
        """
        stack = []
        result = []
        current = self

        while stack or current:
            # Reach the leftmost node of the current node
            while current:
                stack.append(current)
                current = current.left

            # Current is None, so we pop from stack
            current = stack.pop()
            result.append(current.value)

            # Now, visit the right subtree
            current = current.right

        return result
```

### **Example:**
```python
# Constructing the binary tree
root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

print("Iterative In-order Traversal:", root.iterative_inorder())  
# Output: [4, 2, 5, 1, 6, 3, 7]
```

---

### **Conclusion**

Today, we learned how to perform **Pre-order** and **In-order** traversals iteratively. While recursion is a natural fit for tree traversal, iterative methods are crucial when dealing with large trees or when stack overflow is a concern due to deep recursion. Iterative solutions provide better control and avoid the overhead of recursive function calls.

Key takeaways:
- **Pre-order traversal** iteratively uses a stack to visit nodes before their children.
- **In-order traversal** iteratively uses a stack to explore the left subtree before visiting nodes and then moving to the right subtree.