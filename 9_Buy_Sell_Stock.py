class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        # Declaring variables
        buy = 0
        profit = 0

        # Iterating over prices
        for sell in range(1, len(prices)):
            cur_profit = prices[sell] - prices[buy]
            profit = max(profit, cur_profit)
            if prices[sell] < prices[buy]:
                buy = sell

        # Returning the result
        return profit
    
# Time - O(N)
# Space - O(1)