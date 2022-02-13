'''

Problem 494 | Target Sum
https://leetcode.com/problems/target-sum/

'''

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            elif (i, total) in dp:
                return dp[(i, total)]
            else:
                dp[(i, total)] = (backtrack(i + 1, total + nums[i]) +
                                backtrack(i + 1, total - nums[i]))
                return dp[(i, total)]
        return backtrack(0, 0)
        
