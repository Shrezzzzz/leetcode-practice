class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos = 0, 0
        
        for num in nums:
            # Add num to `ones` only if it's not already accounted for in `twos`
            ones = (ones ^ num) & ~twos
            # Add num to `twos` only if it's not already accounted for in `ones`
            twos = (twos ^ num) & ~ones
        
        return ones