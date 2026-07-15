class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place
        instead.
        """
        self.prev = None
        
        def dfs(node):
            if not node:
                return
            
            # Process right first, then left, then node (reverse preorder)
            dfs(node.right)
            dfs(node.left)
            
            node.right = self.prev
            node.left = None
            self.prev = node
        
        dfs(root)