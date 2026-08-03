class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        
        # is_palindrome[i][j] = True if s[i:j+1] is a palindrome
        is_palindrome = [[False] * n for _ in range(n)]
        
        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (end - start <= 2 or is_palindrome[start + 1][end - 1]):
                    is_palindrome[start][end] = True
        
        # min_cuts[i] = minimum cuts needed to partition s[0:i+1]
        min_cuts = [0] * n
        
        for end in range(n):
            if is_palindrome[0][end]:
                min_cuts[end] = 0  # whole prefix is already a palindrome, no cuts needed
            else:
                min_cuts[end] = float('inf')
                for start in range(1, end + 1):
                    if is_palindrome[start][end]:
                        min_cuts[end] = min(min_cuts[end], min_cuts[start - 1] + 1)
        
        return min_cuts[n - 1]