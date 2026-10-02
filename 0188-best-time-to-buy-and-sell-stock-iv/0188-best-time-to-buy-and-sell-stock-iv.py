class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        
        # If k is large enough to allow effectively unlimited transactions,
        # fall back to the simple "sum every positive price increase" strategy
        if k >= n // 2:
            return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, n))
        
        # buy[j] = max profit after the j-th buy (a negative running balance)
        # sell[j] = max profit after the j-th sell
        buy = [float('-inf')] * (k + 1)
        sell = [0] * (k + 1)
        
        for price in prices:
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j - 1] - price)
                sell[j] = max(sell[j], buy[j] + price)
        
        return sell[k]