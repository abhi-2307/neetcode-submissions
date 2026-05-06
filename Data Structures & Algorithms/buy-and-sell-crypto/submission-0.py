class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        max_p = 0
        for i in range(1,len(prices)):
            max_p = max(max_p,prices[i]-mini)
            mini = min(mini,prices[i])
        return max_p
