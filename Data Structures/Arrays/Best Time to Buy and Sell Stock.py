'''

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Brute Force Solution

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if (prices[j] > prices[i]) and (prices[j] - prices[i] > profit):
                    profit = prices[j] - prices[i]
        return profit
