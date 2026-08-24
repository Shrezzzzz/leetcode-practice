class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = []
        
        while columnNumber > 0:
            # Shift into 0-25 range: subtract 1 first because this system
            # is 1-indexed (A=1) instead of 0-indexed, unlike standard base conversion
            columnNumber -= 1
            remainder = columnNumber % 26
            result.append(chr(ord('A') + remainder))
            columnNumber //= 26
        
        return ''.join(reversed(result))