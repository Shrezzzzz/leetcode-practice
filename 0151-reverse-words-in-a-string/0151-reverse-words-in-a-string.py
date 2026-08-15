class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # s.split() with no argument automatically handles multiple spaces
        # and strips leading/trailing whitespace, splitting on any run of spaces
        words = s.split()
        
        return ' '.join(reversed(words))