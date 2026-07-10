class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        # Convert linked list to array, then reuse the array approach
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next
        
        def build(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = build(nums[:mid])
            root.right = build(nums[mid + 1:])
            return root
        
        return build(values)