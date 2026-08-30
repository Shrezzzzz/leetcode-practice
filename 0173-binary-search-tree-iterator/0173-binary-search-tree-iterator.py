class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        # Push every left child along this path, so the top of the
        # stack always holds the next smallest unvisited node
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        
        # After visiting a node, its in-order successor is the leftmost
        # node in its right subtree — push that path onto the stack
        if node.right:
            self._push_left(node.right)
        
        return node.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()