class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []
        path = []
        
        def dfs(node, remaining):
            if not node:
                return
            
            path.append(node.val)
            remaining -= node.val
            
            if not node.left and not node.right and remaining == 0:
                result.append(list(path))  # copy the path before backtracking
            else:
                dfs(node.left, remaining)
                dfs(node.right, remaining)
            
            path.pop()  # backtrack
        
        dfs(root, targetSum)
        return result