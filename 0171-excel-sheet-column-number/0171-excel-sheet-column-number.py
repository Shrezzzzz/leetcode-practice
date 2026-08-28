class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        
        for char in columnTitle:
            digit_value = ord(char) - ord('A') + 1  # 'A' -> 1, ..., 'Z' -> 26
            result = result * 26 + digit_value
        
        return result