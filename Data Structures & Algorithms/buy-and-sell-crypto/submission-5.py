class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        k = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[k]:
                k = i
            else:
                max_profit = max(max_profit, prices[i] - prices[k])

        return max_profit

            
