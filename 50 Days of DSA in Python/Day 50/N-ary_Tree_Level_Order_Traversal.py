class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def level_order(root):
    """
    Perform level order traversal on an N-ary tree.
    """
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            queue.extend(node.children)
        result.append(level)
    
    return result

# Example:
root = Node(1)
root.children = [Node(2), Node(3)]
root.children[0].children = [Node(4)]

print("Level Order Traversal:", level_order(root))  # Output: [[1], [2, 3], [4]]
