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
                # Right half must contain the rotation point (min)
                left = mid + 1
            elif nums[mid] < nums[right]:
                # Right half is sorted normally; min is at mid or earlier
                right = mid
            else:
                # nums[mid] == nums[right]: can't tell which side the
                # minimum is on, so shrink the search space safely by 1
                right -= 1
        
        return nums[left]