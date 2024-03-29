'''

Problem 377 | Combination Sum IV
https://leetcode.com/problems/combination-sum-iv/

'''

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:        
        dp = [0 for i in range(target + 1)]
        for i in nums:
            if i < len(dp):
                dp[i] = 1
        for i in range(1, target + 1):
            for j in nums:
                if i- j > 0:
                    dp[i] += dp[i - j]
        return dp[-1]
      
