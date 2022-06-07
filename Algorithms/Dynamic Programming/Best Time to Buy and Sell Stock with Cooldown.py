'''

Problem 309 | Best Time to Buy and Sell Stock with Cooldown
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        look_up = {}
        
        def backtrack(idx, bought):
            nonlocal look_up
            
            if idx >= len(prices):
                return 0
            
            if (idx, bought) not in look_up:
                a = backtrack(idx + 1, bought)
                if bought:
                    b = backtrack(idx + 2, False) + prices[idx]
                else:
                    b = backtrack(idx + 1, True) - prices[idx]
                
                look_up[(idx, bought)] = max(a, b)
            return look_up[(idx, bought)]
            
        
        return backtrack(0, False)
      
            
