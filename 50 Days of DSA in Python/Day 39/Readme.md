# **Day 39: Binary Trees**

Welcome to Day 39 of **50 Days of DSA in Python**! Today, we dive into **Binary Trees**, one of the most fundamental data structures in computer science. Binary trees are used in a variety of applications, such as expression parsing, decision-making, and implementing hierarchical structures. We will focus on constructing a **Binary Search Tree (BST)** and cover various **traversal techniques** to explore and manipulate the tree.

---

### **Topics Covered:**
- Binary Trees  
- Construct BST  
- Traversal Techniques  

---

## **1. Constructing a Binary Search Tree (BST)**

### **Problem Statement**  
A Binary Search Tree (BST) is a binary tree where for each node:
- The left subtree contains only nodes with values less than the node’s value.
- The right subtree contains only nodes with values greater than the node’s value.
  
This property of BST makes searching for values efficient, with an average time complexity of O(log n) for balanced trees.

### **Approach**

#### **1. Implementing a BST in Python**

We will define a `Node` class to represent each node in the tree and a `BinarySearchTree` class to handle the operations like insertion and searching. The `insert` method will ensure the BST properties are maintained, and we will write a helper method to traverse the tree.

#### **Code:**
```python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """
        Insert a new key into the Binary Search Tree.
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        """
        Helper method for recursive insertion.
        """
        if key < root.value:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        elif key > root.value:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def search(self, key):
        """
        Search for a key in the BST. Returns True if found, otherwise False.
        """
        return self._search(self.root, key)

    def _search(self, root, key):
        """
        Helper method for recursive search.
        """
        if root is None or root.value == key:
            return root is not None
        if key < root.value:
            return self._search(root.left, key)
        return self._search(root.right, key)
```

### **Example:**
```python
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print(bst.search(40))  # Output: True
print(bst.search(25))  # Output: False
```

---

## **2. Traversal Techniques**

### **Problem Statement**  
Traversal refers to visiting each node in a tree in a specific order. The common types of tree traversal are:
- **In-order traversal**: Left subtree → Node → Right subtree
- **Pre-order traversal**: Node → Left subtree → Right subtree
- **Post-order traversal**: Left subtree → Right subtree → Node

Each traversal has different applications, such as printing the values of the tree in sorted order (in-order) or copying the tree (pre-order).

### **Approach**

We will implement all three common traversal techniques using recursion.

#### **1. In-order Traversal**
In in-order traversal, we first visit the left subtree, then the root, and finally the right subtree.

#### **2. Pre-order Traversal**
In pre-order traversal, we visit the root node first, followed by the left subtree, and then the right subtree.

#### **3. Post-order Traversal**
In post-order traversal, we visit the left subtree first, followed by the right subtree, and finally the root node.

#### **Code:**
```python
class BinarySearchTree:
    # Previous methods omitted for brevity...
    
    def inorder(self, root):
        """
        In-order Traversal: Left → Node → Right
        """
        return self._inorder(root)

    def _inorder(self, root):
        result = []
        if root:
            result += self._inorder(root.left)
            result.append(root.value)
            result += self._inorder(root.right)
        return result

    def preorder(self, root):
        """
        Pre-order Traversal: Node → Left → Right
        """
        return self._preorder(root)

    def _preorder(self, root):
        result = []
        if root:
            result.append(root.value)
            result += self._preorder(root.left)
            result += self._preorder(root.right)
        return result

    def postorder(self, root):
        """
        Post-order Traversal: Left → Right → Node
        """
        return self._postorder(root)

    def _postorder(self, root):
        result = []
        if root:
            result += self._postorder(root.left)
            result += self._postorder(root.right)
            result.append(root.value)
        return result
```

### **Example:**
```python
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("In-order Traversal:", bst.inorder(bst.root))   # Output: [20, 30, 40, 50, 60, 70, 80]
print("Pre-order Traversal:", bst.preorder(bst.root)) # Output: [50, 30, 20, 40, 70, 60, 80]
print("Post-order Traversal:", bst.postorder(bst.root)) # Output: [20, 40, 30, 60, 80, 70, 50]
```

---

### **Conclusion**

Today, we explored **Binary Search Trees (BST)** and covered:

1. **Constructing a BST**: We learned how to build a binary search tree and insert elements while maintaining its properties.

2. **Traversal Techniques**: We implemented the common traversal methods: **In-order**, **Pre-order**, and **Post-order**. Each traversal serves different purposes, like sorting elements (in-order) or copying the tree (pre-order).

By understanding BSTs and traversal methods, you can solve problems involving hierarchical data and improve your ability to work with trees efficiently.