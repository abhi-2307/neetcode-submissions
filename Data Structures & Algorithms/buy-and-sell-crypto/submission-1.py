class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheap = prices[0]
        profit = 0
        for i in range(len(prices)):
            cheap = min(cheap, prices[i])
            profit = max(profit, prices[i] - cheap)
        return profit
        