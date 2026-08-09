class Solution(object):
    def preorderTraversal(self, root):
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
            
            # Push right FIRST so left gets popped (and processed) first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result