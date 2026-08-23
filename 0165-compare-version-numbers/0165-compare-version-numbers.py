class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        revisions1 = version1.split('.')
        revisions2 = version2.split('.')
        
        # Pad the shorter list with "0" so both lists have equal length
        n = max(len(revisions1), len(revisions2))
        
        for i in range(n):
            # int() naturally strips leading zeros (e.g., "001" -> 1)
            rev1 = int(revisions1[i]) if i < len(revisions1) else 0
            rev2 = int(revisions2[i]) if i < len(revisions2) else 0
            
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
        
        return 0