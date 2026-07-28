class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        
        leftmost = root
        
        while leftmost:
            # Dummy node to build the next level's linked list
            dummy = Node(0)
            tail = dummy
            
            node = leftmost
            while node:
                if node.left:
                    tail.next = node.left
                    tail = tail.next
                if node.right:
                    tail.next = node.right
                    tail = tail.next
                node = node.next
            
            leftmost = dummy.next
        
        return root