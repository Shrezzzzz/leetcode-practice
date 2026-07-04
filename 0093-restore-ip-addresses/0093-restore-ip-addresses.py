class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        n = len(s)
        
        def valid(segment):
            if len(segment) > 1 and segment[0] == '0':
                return False
            return 0 <= int(segment) <= 255
        
        def backtrack(start, parts):
            if len(parts) == 4:
                if start == n:
                    res.append('.'.join(parts))
                return
            for length in range(1, 4):
                if start + length > n:
                    break
                segment = s[start:start + length]
                if valid(segment):
                    backtrack(start + length, parts + [segment])
        
        backtrack(0, [])
        return res