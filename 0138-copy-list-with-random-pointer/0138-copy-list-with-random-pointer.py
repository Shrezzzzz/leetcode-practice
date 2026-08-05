class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        # Step 1: interleave cloned nodes into the original list:
        # orig1 -> clone1 -> orig2 -> clone2 -> ...
        node = head
        while node:
            clone = Node(node.val)
            clone.next = node.next
            node.next = clone
            node = clone.next
        
        # Step 2: set random pointers on the clones using the interleaving
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next
        
        # Step 3: unweave the two lists back apart
        node = head
        clone_head = head.next
        while node:
            clone = node.next
            node.next = clone.next
            clone.next = clone.next.next if clone.next else None
            node = node.next
        
        return clone_head