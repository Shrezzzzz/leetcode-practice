class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        
        # dp[i][j] = number of distinct subsequences of s[:i] that equal t[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Empty t is a subsequence of any prefix of s exactly one way
        for i in range(m + 1):
            dp[i][0] = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Option 1: skip s[i-1], don't use it to match t[j-1]
                dp[i][j] = dp[i - 1][j]
                
                # Option 2: if characters match, we can also use s[i-1] to match t[j-1]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        
        return dp[m][n]