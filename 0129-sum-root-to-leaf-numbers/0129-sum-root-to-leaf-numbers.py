class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, current_number):
            if not node:
                return 0
            
            current_number = current_number * 10 + node.val
            
            # If it's a leaf, this path is complete — return its number
            if not node.left and not node.right:
                return current_number
            
            return dfs(node.left, current_number) + dfs(node.right, current_number)
        
        return dfs(root, 0)