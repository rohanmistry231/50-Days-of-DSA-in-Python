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
