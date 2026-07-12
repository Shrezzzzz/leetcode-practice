class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        # If it's a leaf, check if remaining sum matches this node's value
        if not root.left and not root.right:
            return targetSum == root.val
        
        remaining = targetSum - root.val
        
        return (self.hasPathSum(root.left, remaining) or 
                self.hasPathSum(root.right, remaining))