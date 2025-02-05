from collections import deque
from logging import root

def zigzag_traversal(root):
    """
    Perform a Zigzag (Spiral) level order traversal of a binary tree.
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level = []
        level_length = len(queue)
        
        for _ in range(level_length):
            node = queue.popleft()
            level.append(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # If the current level's traversal is from right to left, reverse the level
        if not left_to_right:
            level.reverse()
        
        result.append(level)
        
        # Toggle the direction for the next level
        left_to_right = not left_to_right
    
    return result

# Example:
print("Zigzag Traversal:", zigzag_traversal(root))
