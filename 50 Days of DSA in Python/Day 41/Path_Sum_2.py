class BinaryTree:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

    def path_sum_2(self, target_sum):
        """
        Find all root-to-leaf paths where the sum equals target_sum.
        """
        result = []
        self._dfs(self, target_sum, [], result)
        return result

    def _dfs(self, node, remaining_sum, current_path, result):
        if not node:
            return
        
        # Include the current node in the path
        current_path.append(node.value)
        
        # If it's a leaf node and the sum matches, add path to result
        if not node.left and not node.right and remaining_sum == node.value:
            result.append(list(current_path))
        else:
            # Continue to explore left and right subtrees
            self._dfs(node.left, remaining_sum - node.value, current_path, result)
            self._dfs(node.right, remaining_sum - node.value, current_path, result)

        # Backtrack
        current_path.pop()
