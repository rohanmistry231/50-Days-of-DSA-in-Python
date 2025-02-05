from collections import deque
from logging import root

def right_view(root):
    """
    Return the right view of a binary tree.
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_length = len(queue)
        
        for i in range(level_length):
            node = queue.popleft()
            
            # If it is the last node of the level, add it to the result
            if i == level_length - 1:
                result.append(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

# Example:
print("Right View:", right_view(root))