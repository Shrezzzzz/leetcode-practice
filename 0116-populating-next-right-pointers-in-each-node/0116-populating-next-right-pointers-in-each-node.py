class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        
        leftmost = root
        
        # Process level by level, using already-set next pointers
        # of the current level to reach across to the next level
        while leftmost.left:
            head = leftmost
            while head:
                # Connect the two children of this node
                head.left.next = head.right
                
                # Connect right child to the left child of the next node
                if head.next:
                    head.right.next = head.next.left
                
                head = head.next
            
            leftmost = leftmost.left
        
        return root