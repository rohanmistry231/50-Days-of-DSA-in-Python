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
