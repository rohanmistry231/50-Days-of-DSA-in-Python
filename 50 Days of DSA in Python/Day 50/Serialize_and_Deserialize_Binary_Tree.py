class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        def helper(node):
            if not node:
                return "#"
            return str(node.value) + "," + helper(node.left) + "," + helper(node.right)
        
        return helper(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        values = data.split(",")
        def helper():
            val = values.pop(0)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node
        
        return helper()

# Example:
codec = Codec()
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(5)

serialized = codec.serialize(tree)
print("Serialized:", serialized)  # Output: "1,2,#,#,3,4,#,#,5,#,#"

deserialized = codec.deserialize(serialized)
print("Deserialized root value:", deserialized.value)  # Output: 1
