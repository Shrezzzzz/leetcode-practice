class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        
        result = []
        
        # Determine overall sign
        if (numerator < 0) != (denominator < 0):
            result.append('-')
        
        # Work with absolute values from here on
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Integer part
        integer_part = numerator // denominator
        result.append(str(integer_part))
        
        remainder = numerator % denominator
        if remainder == 0:
            return ''.join(result)
        
        result.append('.')
        
        # Track each remainder's position in the fractional string,
        # so if a remainder repeats, we know exactly where to insert parentheses
        seen_remainders = {}
        fractional_part = []
        
        while remainder != 0:
            if remainder in seen_remainders:
                insert_pos = seen_remainders[remainder]
                fractional_part.insert(insert_pos, '(')
                fractional_part.append(')')
                break
            
            seen_remainders[remainder] = len(fractional_part)
            remainder *= 10
            fractional_part.append(str(remainder // denominator))
            remainder %= denominator
        
        result.append(''.join(fractional_part))
        return ''.join(result)