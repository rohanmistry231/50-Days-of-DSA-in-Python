# **Day 49: Binary Trees - Lowest Common Ancestor of Binary Tree & Unique BST 1**

Welcome to Day 49 of **50 Days of DSA in Python**! Today, we will focus on solving two important problems related to binary trees: **Lowest Common Ancestor of Binary Tree** and **Unique BST 1**. These problems test your understanding of tree traversal and construction techniques, as well as handling various constraints for tree structure generation.

---

### **Topics Covered:**
- Lowest Common Ancestor of Binary Tree
- Unique BST 1

---

## **1. Lowest Common Ancestor of Binary Tree**

### **Problem Statement**  
Given a **binary tree**, find the **lowest common ancestor (LCA)** of two given nodes. The lowest common ancestor of two nodes `p` and `q` is defined as the deepest node that is an ancestor of both `p` and `q`.

Unlike the BST version (Day 48), where we exploit the BST properties (left is smaller, right is larger), the binary tree doesn't have such properties. Therefore, the solution must rely on tree traversal and backtracking.

For example:
- Input:
  ```
        3
       / \
      5   1
     / \ / \
    6  2 0  8
       / \
      7   4
  ```
  `p = 5`, `q = 1`
- Output: `3`

- Input:  
  `p = 5`, `q = 4`
- Output: `5`

### **Approach**

1. Perform a **post-order traversal** of the tree. If a node is `None`, return `None`.
2. If a node is either `p` or `q`, return that node.
3. Recursively find the LCA in the left and right subtrees.
4. If one node is found in the left and the other in the right subtree, then the current node is the LCA.
5. If both nodes are found in one subtree, return the non-`None` value.

#### **Code:**
```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def lowest_common_ancestor(root, p, q):
    """
    Find the lowest common ancestor of two nodes in a binary tree.
    """
    if not root:
        return None
    
    if root == p or root == q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root
    
    return left if left else right

# Example:
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

p = root.left  # Node 5
q = root.right  # Node 1

print("LCA:", lowest_common_ancestor(root, p, q).value)  # Output: 3
```

### **Explanation:**
- The function performs a post-order traversal to check if either of the nodes `p` or `q` is found in the left or right subtrees.
- If one node is found in both subtrees, the current node is returned as the LCA.
- If both nodes are found in one subtree, that subtree's result is returned.

---

## **2. Unique BST 1**

### **Problem Statement**  
Given an integer `n`, generate all **unique binary search trees (BSTs)** that can be constructed using node values from `1` to `n`. The key difference from **Unique BST 2** (Day 48) is that this version focuses on generating the unique BSTs without considering the overall tree structure constraints (i.e., no extra constraints).

For example:
- Input: `n = 3`
- Output:  
  ```
  [ [1, null, 2, null, 3], [3, 2, null, 1] ]
  ```
  These represent two unique BSTs that can be created using nodes `1`, `2`, and `3`.

### **Approach**

1. Use a **recursive approach** to build all possible unique BSTs:
   - For each node `i` from `1` to `n`, treat `i` as the root of the tree.
   - Recursively generate all left subtrees using values `1` to `i-1` and all right subtrees using values `i+1` to `n`.
   - Combine the left and right subtrees with `i` as the root to form all possible unique BSTs.

#### **Code:**
```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def generate_trees(n):
    """
    Generate all unique BSTs that store values 1 to n.
    """
    def build_tree(start, end):
        if start > end:
            return [None]
        
        trees = []
        for i in range(start, end + 1):
            # Generate all left and right subtrees
            left_trees = build_tree(start, i - 1)
            right_trees = build_tree(i + 1, end)
            
            # Combine them to form trees with root i
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    trees.append(root)
        
        return trees

    return build_tree(1, n)

# Example:
trees = generate_trees(3)
print(f"Number of unique BSTs: {len(trees)}")  # Output: 5
```

### **Explanation:**
- The function `build_tree(start, end)` recursively constructs all unique BSTs for a given range `[start, end]`.
- For each value `i` in the range, we generate all possible left and right subtrees and combine them with `i` as the root to generate all unique BSTs.

---

### **Conclusion**

Today, we worked on:
- The **Lowest Common Ancestor of Binary Tree**, which finds the deepest node that is an ancestor of two given nodes using tree traversal and backtracking.
- **Unique BST 1**, which generates all unique binary search trees using the numbers from `1` to `n` recursively by considering each number as the root.

Key takeaways:
- The **Lowest Common Ancestor of Binary Tree** approach uses post-order traversal to explore both left and right subtrees.
- **Unique BST 1** relies on recursive tree construction and is based on the idea of generating all possible combinations of left and right subtrees for every node as the root.