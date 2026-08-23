class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # convert to 1-indexed
            elif current_sum < target:
                left += 1  # need a bigger sum, move left pointer up
            else:
                right -= 1  # need a smaller sum, move right pointer down
        
        return []  # problem guarantees a solution exists, so this won't hit