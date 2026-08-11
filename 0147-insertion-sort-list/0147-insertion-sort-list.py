class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Dummy node simplifies inserting at the very front of the sorted list
        dummy = ListNode(0)
        current = head
        
        while current:
            next_node = current.next  # save before we relink current
            
            # Find the insertion point: the last node in the sorted portion
            # whose value is <= current.val
            prev = dummy
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            
            # Insert current between prev and prev.next
            current.next = prev.next
            prev.next = current
            
            current = next_node
        
        return dummy.next