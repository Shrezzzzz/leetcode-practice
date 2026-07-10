class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not inorder or not postorder:
            return None
        
        inorder_index = {val: i for i, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1
        
        def build(left, right):
            if left > right:
                return None
            
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)
            
            mid = inorder_index[root_val]
            
            # Build right subtree FIRST since postorder ends with: ...left, right, root
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)
            
            return root
        
        return build(0, len(inorder) - 1)