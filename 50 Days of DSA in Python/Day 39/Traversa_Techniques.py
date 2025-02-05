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
