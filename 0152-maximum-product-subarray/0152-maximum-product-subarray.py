class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = nums[0]
        current_max = nums[0]
        current_min = nums[0]
        
        for num in nums[1:]:
            # A negative number can flip max and min, so consider both
            # possibilities BEFORE updating (using the OLD current_max/current_min)
            candidates = (num, current_max * num, current_min * num)
            current_max = max(candidates)
            current_min = min(candidates)
            
            max_so_far = max(max_so_far, current_max)
        
        return max_so_far