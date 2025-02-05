class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def generate_trees(n):
    """
    Generate all unique BSTs that store values 1 to n.
    """
    def build_tree(start, end):
        if start > end:
            return [None]
        
        trees = []
        for i in range(start, end + 1):
            # Generate all left and right subtrees
            left_trees = build_tree(start, i - 1)
            right_trees = build_tree(i + 1, end)
            
            # Combine them to form trees with root i
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    trees.append(root)
        
        return trees

    return build_tree(1, n)

# Example:
trees = generate_trees(3)
print(f"Number of unique BSTs: {len(trees)}")  # Output: 5
