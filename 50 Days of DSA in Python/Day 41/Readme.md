# **Day 41: Post-Order Traversal Iterative & Path Sum 2**

Welcome to Day 41 of **50 Days of DSA in Python**! Today, we focus on solving tree traversal problems and path sum problems. We will cover **Post-order Traversal** using an **iterative** approach and solve the **Path Sum 2** problem, which involves finding all root-to-leaf paths that sum up to a target value.

---

### **Topics Covered:**
- Post-order Traversal (Iterative)  
- Path Sum 2

---

## **1. Iterative Post-order Traversal**

### **Problem Statement**  
In Post-order traversal, we recursively visit the **left subtree**, then the **right subtree**, and finally process the **node**. Although recursion is the natural way to implement Post-order traversal, it can be done iteratively using two stacks or a modified approach with one stack.

### **Approach**

We can achieve Post-order traversal iteratively by using two stacks:
1. **First Stack**: Used for storing nodes.
2. **Second Stack**: Used to ensure the right children are processed after the left children.

Alternatively, we can use a single stack and a **previous node pointer** to ensure we process the node after visiting both its left and right children.

#### **Code:**
```python
class BinaryTree:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

    def iterative_postorder(self):
        """
        Iterative Post-order Traversal: Left → Right → Node
        """
        if not self:
            return []

        stack1 = [self]
        stack2 = []
        result = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        while stack2:
            result.append(stack2.pop().value)

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

print("Iterative Post-order Traversal:", root.iterative_postorder())  
# Output: [4, 5, 2, 6, 7, 3, 1]
```

---

## **2. Path Sum 2**

### **Problem Statement**  
Given a binary tree and a sum, the task is to find all root-to-leaf paths where the sum of the node values along the path equals the given sum.

### **Approach**

To solve the **Path Sum 2** problem, we use Depth-First Search (DFS):
1. We explore each node and check if we can reach a leaf node with the given sum.
2. If we find a leaf node and the remaining sum is 0, we add the current path to the result.
3. We backtrack to explore other paths.

DFS allows us to explore all possible paths, and we store each valid path that sums to the target.

#### **Code:**
```python
class BinaryTree:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

    def path_sum_2(self, target_sum):
        """
        Find all root-to-leaf paths where the sum equals target_sum.
        """
        result = []
        self._dfs(self, target_sum, [], result)
        return result

    def _dfs(self, node, remaining_sum, current_path, result):
        if not node:
            return
        
        # Include the current node in the path
        current_path.append(node.value)
        
        # If it's a leaf node and the sum matches, add path to result
        if not node.left and not node.right and remaining_sum == node.value:
            result.append(list(current_path))
        else:
            # Continue to explore left and right subtrees
            self._dfs(node.left, remaining_sum - node.value, current_path, result)
            self._dfs(node.right, remaining_sum - node.value, current_path, result)

        # Backtrack
        current_path.pop()
```

### **Example:**
```python
# Constructing the binary tree
root = BinaryTree(5)
root.left = BinaryTree(4)
root.right = BinaryTree(8)
root.left.left = BinaryTree(11)
root.left.left.left = BinaryTree(7)
root.left.left.right = BinaryTree(2)
root.right.left = BinaryTree(13)
root.right.right = BinaryTree(4)
root.right.right.left = BinaryTree(5)
root.right.right.right = BinaryTree(1)

# Find all paths with a sum of 22
print("Paths with sum 22:", root.path_sum_2(22))  
# Output: [[5, 4, 11, 2], [5, 8, 4, 5]]
```

---

### **Conclusion**

In today's session, we learned how to perform:
- **Post-order traversal iteratively** using two stacks for efficient tree traversal, ensuring nodes are processed after their left and right children.
- **Path Sum 2**, which involves finding all root-to-leaf paths whose sum equals the target. This was done using a DFS approach with backtracking to explore each possible path.

Key takeaways:
- **Post-order traversal (iterative)** ensures nodes are processed after their children by using a second stack.
- **Path Sum 2** utilizes DFS to find all paths that sum to a target value, employing backtracking to ensure all paths are explored.