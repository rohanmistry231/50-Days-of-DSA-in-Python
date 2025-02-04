# **Day 48: Binary Trees - Lowest Common Ancestor of BST & Unique BST 2**

Welcome to Day 48 of **50 Days of DSA in Python**! Today, we will dive into two key problems related to binary search trees (BST): **Lowest Common Ancestor of BST** and **Unique BST 2**. These problems explore the concepts of finding common ancestors in a BST and generating unique binary search trees given certain constraints.

---

### **Topics Covered:**
- Lowest Common Ancestor of BST
- Unique BST 2

---

## **1. Lowest Common Ancestor of BST**

### **Problem Statement**  
Given a **binary search tree (BST)**, find the **lowest common ancestor (LCA)** of two given nodes. The lowest common ancestor of two nodes `p` and `q` is the deepest node that is an ancestor of both `p` and `q`.

For example:
- Input:  
  ```
        6
       / \
      2   8
     / \ / \
    0  4 7  9
      / \
     3  5
  ```
  `p = 2`, `q = 8`
- Output: `6`

- Input:  
  `p = 2`, `q = 4`
- Output: `2`

### **Approach**

1. Since the given tree is a BST, the LCA of `p` and `q` must lie in the following way:
   - If both `p` and `q` are smaller than the root, the LCA must be in the left subtree.
   - If both `p` and `q` are greater than the root, the LCA must be in the right subtree.
   - If one of `p` or `q` is smaller and the other is greater than the root, the current root is the LCA.
   
2. Use a **recursive** or **iterative** approach to traverse the tree until the LCA is found.

#### **Code:**
```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def lowest_common_ancestor(root, p, q):
    """
    Find the lowest common ancestor (LCA) of two nodes in a BST.
    """
    if not root:
        return None
    
    # If both nodes are smaller, go left
    if p.value < root.value and q.value < root.value:
        return lowest_common_ancestor(root.left, p, q)
    
    # If both nodes are larger, go right
    if p.value > root.value and q.value > root.value:
        return lowest_common_ancestor(root.right, p, q)
    
    # Otherwise, root is the LCA
    return root

# Example:
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

p = root.left  # Node 2
q = root.right  # Node 8

print("LCA:", lowest_common_ancestor(root, p, q).value)  # Output: 6
```

### **Explanation:**
- The function traverses the tree based on the values of `p` and `q`, checking if they are smaller or larger than the root.
- The first time it finds that one node is smaller and the other is larger, it returns the current node as the LCA.

---

## **2. Unique BST 2**

### **Problem Statement**  
Given a number `n`, generate all **unique binary search trees (BSTs)** that can be formed with `n` nodes where the node values range from `1` to `n`. Unlike the first version of the problem (Unique BST 1), where the range is continuous from `1` to `n`, this problem requires a more flexible approach where each unique BST is distinct in terms of structure.

For example:
- Input: `n = 3`
- Output:  
  ```
  [ [1, null, 2, null, 3], [3, 2, null, 1] ]
  ```
  These represent two unique BSTs that can be created using nodes `1`, `2`, and `3`.

### **Approach**

1. The idea is to recursively consider each number `i` from `1` to `n` as the root of the tree.
2. For each number `i`, construct the left and right subtrees from the remaining numbers, making sure that the left subtree contains values less than `i` and the right subtree contains values greater than `i`.
3. Use **recursive generation** to create all possible unique BSTs by combining left and right subtrees for each root.

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
- For each value `i` between `start` and `end`, we generate all possible left and right subtrees and combine them with `i` as the root.
- This results in all unique BSTs for the given range.

---

### **Conclusion**

In today’s session, we:
- Implemented the **Lowest Common Ancestor of BST** algorithm to find the deepest node that is an ancestor of both given nodes in a binary search tree.
- Implemented **Unique BST 2**, a recursive approach to generate all unique BSTs that can be formed with `n` nodes.

Key takeaways:
- The **Lowest Common Ancestor of BST** relies on the properties of BSTs, where values to the left are smaller and values to the right are larger.
- **Unique BST 2** generates all possible BSTs recursively by considering each node as a potential root and generating left and right subtrees.