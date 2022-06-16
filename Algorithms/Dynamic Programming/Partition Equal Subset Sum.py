'''

Problem 416 | Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/

'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:            
        res = sum(nums)
        if res % 2:
            return False
        
        res /= 2
        t1 = set([0])
        
        for n in nums:
            if res in t1:
                return True
            t2 = set(t + n for t in t1)
            t1.update(t2)
            
        return False
        
