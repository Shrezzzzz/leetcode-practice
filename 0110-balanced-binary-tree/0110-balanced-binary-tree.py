class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(node):
            # Returns height if balanced, -1 if not balanced
            if not node:
                return 0
            
            left_height = check(node.left)
            if left_height == -1:
                return -1
            
            right_height = check(node.right)
            if right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1
            
            return 1 + max(left_height, right_height)
        
        return check(root) != -1