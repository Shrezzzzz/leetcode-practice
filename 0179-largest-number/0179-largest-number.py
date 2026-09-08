from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Convert all numbers to strings so we can concatenate and compare them
        str_nums = [str(num) for num in nums]
        
        def compare(a, b):
            # Compare by which concatenation order produces a larger result:
            # "ba" vs "ab" — if ba > ab, then b should come before a
            if a + b > b + a:
                return -1  # a should come before b
            elif a + b < b + a:
                return 1   # b should come before a
            else:
                return 0
        
        str_nums.sort(key=cmp_to_key(compare))
        
        result = ''.join(str_nums)
        
        # Handle the all-zeros edge case (e.g., [0, 0] should return "0", not "00")
        if result[0] == '0':
            return '0'
        
        return result