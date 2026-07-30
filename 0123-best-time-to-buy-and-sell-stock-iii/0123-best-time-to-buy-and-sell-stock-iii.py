class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Track state after each possible transaction stage:
        buy1 = float('-inf')   # max profit after 1st buy (profit is negative = cost)
        sell1 = 0               # max profit after 1st sell
        buy2 = float('-inf')   # max profit after 2nd buy
        sell2 = 0               # max profit after 2nd sell
        
        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)
        
        return sell2