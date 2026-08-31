class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        
        # dp[i][j] = minimum HP needed upon ENTERING room (i, j) 
        # to survive the rest of the path to the princess
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        # Base case: from the princess's room, you need at least 1 HP
        # remaining AFTER stepping out (conceptually, past the bottom-right)
        dp[m][n - 1] = 1
        dp[m - 1][n] = 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Minimum HP needed AFTER this room, to survive the best of the two paths onward
                min_hp_after = min(dp[i + 1][j], dp[i][j + 1])
                
                # HP needed upon ENTERING this room = (needed after) - (this room's effect),
                # but never less than 1 (you must always have positive HP)
                dp[i][j] = max(1, min_hp_after - dungeon[i][j])
        
        return dp[0][0]