class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        # Step 1: split the list into two halves using slow/fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None  # cut the list into two
        
        # Step 2: recursively sort each half
        left = self.sortList(head)
        right = self.sortList(second_half)
        
        # Step 3: merge the two sorted halves
        return self._merge(left, right)
    
    def _merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        # Attach whichever list still has remaining nodes
        tail.next = l1 if l1 else l2
        
        return dummy.next