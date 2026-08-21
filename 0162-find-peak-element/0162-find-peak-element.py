class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[mid + 1]:
                # We're on a downward slope from mid to mid+1, so a peak
                # must exist at mid or somewhere to its left
                right = mid
            else:
                # nums[mid] < nums[mid+1]: we're on an upward slope,
                # so a peak must exist somewhere to the right of mid
                left = mid + 1
        
        return left