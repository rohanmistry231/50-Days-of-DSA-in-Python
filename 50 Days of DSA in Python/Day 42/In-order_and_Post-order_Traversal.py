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
