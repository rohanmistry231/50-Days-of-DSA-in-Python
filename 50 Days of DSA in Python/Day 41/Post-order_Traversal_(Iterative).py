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
