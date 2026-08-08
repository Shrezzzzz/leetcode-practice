class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        
        # Phase 1: detect whether a cycle exists (Floyd's algorithm)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None  # fast hit the end — no cycle
        
        # Phase 2: find the cycle's starting node
        # Move one pointer back to head; advance both one step at a time
        pointer = head
        while pointer != slow:
            pointer = pointer.next
            slow = slow.next
        
        return pointer