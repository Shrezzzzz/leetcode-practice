class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        power_of_five = 5
        
        while power_of_five <= n:
            count += n // power_of_five
            power_of_five *= 5
        
        return count