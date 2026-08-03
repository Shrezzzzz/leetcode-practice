class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_surplus = 0
        current_surplus = 0
        start_index = 0
        
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_surplus += diff
            current_surplus += diff
            
            # If the tank goes negative, this start point (and everything
            # since the last reset) can't work — try starting fresh from i+1
            if current_surplus < 0:
                start_index = i + 1
                current_surplus = 0
        
        return start_index if total_surplus >= 0 else -1