class Solution:
    def maxProfit(self, prices):
        min_price = 9223372036854775807
        max_profit = 0
        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            max_profit = max(prices[i] - min_price, max_profit)
        return max_profit