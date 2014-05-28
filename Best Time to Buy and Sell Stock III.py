class Solution:
    def maxProfit(self, prices):
        min_price, max_profit = 9223372036854775807, 0
        profits_before = [0 for i in range(len(prices))]
        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            max_profit = max(prices[i] - min_price, max_profit)
            profits_before[i] = max_profit
        max_price, max_profit = -9223372036854775808, 0
        profits_after = [0 for i in range(len(prices))]
        for i in reversed(range(len(prices))):
            max_price = max(prices[i], max_price)
            max_profit = max(max_price - prices[i], max_profit)
            profits_after[i] = max_profit
        return reduce(lambda acc, i: max(profits_before[i] + profits_after[i], acc), range(len(prices)), 0)