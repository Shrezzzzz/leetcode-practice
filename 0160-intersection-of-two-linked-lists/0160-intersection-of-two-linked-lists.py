class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        pointerA = headA
        pointerB = headB
        
        # When one pointer reaches the end, redirect it to the OTHER list's head.
        # This equalizes the total distance traveled by both pointers,
        # so they arrive at the intersection point (or None) at the same time.
        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA
        
        return pointerA