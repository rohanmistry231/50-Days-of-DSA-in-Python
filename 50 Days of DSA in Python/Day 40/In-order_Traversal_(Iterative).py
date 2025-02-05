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
