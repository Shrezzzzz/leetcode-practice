class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        
        result = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            # Push left first, then right (opposite of preorder),
            # so they come off in right-then-left order
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        # We built root -> right -> left; reverse it to get left -> right -> root
        return result[::-1]