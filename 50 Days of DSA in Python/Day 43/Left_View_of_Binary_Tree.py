from collections import deque
from logging import root

def left_view(root):
    """
    Return the left view of a binary tree.
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_length = len(queue)
        
        for i in range(level_length):
            node = queue.popleft()
            
            # If it is the first node of the level, add it to the result
            if i == 0:
                result.append(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

# Example:
print("Left View:", left_view(root))