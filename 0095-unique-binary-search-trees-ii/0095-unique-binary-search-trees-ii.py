# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        if n == 0:
            return []
        
        def build(lo, hi):
            if lo > hi:
                return [None]
            trees = []
            for root_val in range(lo, hi + 1):
                left_trees = build(lo, root_val - 1)
                right_trees = build(root_val + 1, hi)
                for l in left_trees:
                    for r in right_trees:
                        node = TreeNode(root_val)
                        node.left = l
                        node.right = r
                        trees.append(node)
            return trees
        
        return build(1, n)