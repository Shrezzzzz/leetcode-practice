class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float('-inf')
        
        def max_gain(node):
            if not node:
                return 0
            
            # Only take a child's contribution if it's positive; otherwise skip it
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # Best path THROUGH this node (as the "peak"), using both children
            price_newpath = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, price_newpath)
            
            # But a node can only return ONE branch upward to its parent,
            # since a path can't branch in two directions past this point
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum