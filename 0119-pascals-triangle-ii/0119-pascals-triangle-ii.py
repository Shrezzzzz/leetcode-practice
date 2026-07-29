class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1] * (rowIndex + 1)
        
        for i in range(1, rowIndex + 1):
            # Update right-to-left so we don't overwrite values we still need
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
        
        return row