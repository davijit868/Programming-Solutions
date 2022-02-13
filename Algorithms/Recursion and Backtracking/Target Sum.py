'''

Problem 494 | Target Sum
https://leetcode.com/problems/target-sum/

'''

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        def backtrack(start, total):
            nonlocal count
            if start == len(nums):
                if total == target:
                    count += 1
                return
            backtrack(start + 1, total + nums[start])
            backtrack(start + 1, total - nums[start])
            
        backtrack(0, 0)
        return count
        
