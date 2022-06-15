'''

Problem 416 | Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/

'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        else:
            target = total // 2
        
        def recursion(idx, total):
            if total == target:
                return True
            if idx >= len(nums) or total > target:
                return False
            return recursion(idx + 1, total + nums[idx]) or recursion(idx + 1, total)
        
        return recursion(0, 0)
            
            
