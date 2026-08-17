class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                # Minimum must be in the right half (mid is part of the
                # larger, "unrotated" left segment, so exclude it)
                left = mid + 1
            else:
                # nums[mid] <= nums[right] means the right half is sorted
                # normally, so the minimum is at mid or somewhere to its left
                right = mid
        
        return nums[left]