# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        state = {'first': None, 'second': None, 'prev': None}
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if state['prev'] and state['prev'].val > node.val:
                if not state['first']:
                    state['first'] = state['prev']
                state['second'] = node
            state['prev'] = node
            inorder(node.right)
        
        inorder(root)
        state['first'].val, state['second'].val = state['second'].val, state['first'].val