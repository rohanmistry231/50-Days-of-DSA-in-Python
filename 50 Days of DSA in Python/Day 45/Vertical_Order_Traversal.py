from collections import defaultdict, deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def vertical_order_traversal(root):
    """
    Perform vertical order traversal of a binary tree.
    """
    if not root:
        return []

    # A dictionary to hold nodes at each horizontal distance
    column_map = defaultdict(list)
    
    # Queue for level order traversal with horizontal distance
    queue = deque([(root, 0)])  # (node, horizontal_distance)
    
    while queue:
        node, hd = queue.popleft()
        column_map[hd].append(node.value)
        
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    
    # Sort the keys (horizontal distances) and prepare the result
    sorted_columns = sorted(column_map.keys())
    result = [column_map[hd] for hd in sorted_columns]
    
    return result

# Example:
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print("Vertical Order Traversal:", vertical_order_traversal(root))
