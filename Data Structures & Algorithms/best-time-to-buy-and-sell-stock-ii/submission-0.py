class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for ind,val in enumerate(prices):
            if ind>0:
                if val > prices[ind-1]:
                    profit+=(val-prices[ind-1])
        return profit