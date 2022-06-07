'''

Problem 309 | Best Time to Buy and Sell Stock with Cooldown
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        
        def backtrack(idx, bought, profit):
            nonlocal max_profit
            
            if profit > max_profit:
                max_profit = profit
            
            if idx >= len(prices):
                return 
            
            backtrack(idx + 1, bought, profit)
            if bought:
                backtrack(idx + 2, False, profit + prices[idx])
            else:
                backtrack(idx + 1, True, profit - prices[idx])
        
        backtrack(0, True, -prices[0])
        backtrack(0, False, 0)
        
        return max_profit
            
