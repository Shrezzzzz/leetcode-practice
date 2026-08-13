from collections import defaultdict

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        n = len(points)
        if n <= 2:
            return n
        
        max_points = 1
        
        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]
            
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                
                g = gcd(dx, dy)
                if g != 0:
                    dx //= g
                    dy //= g
                
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                
                slopes[(dx, dy)] += 1
            
            if slopes:
                max_points = max(max_points, max(slopes.values()) + 1)
        
        return max_points