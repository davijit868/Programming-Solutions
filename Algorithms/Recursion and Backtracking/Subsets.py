'''

Problem 78 | Subsets
https://leetcode.com/problems/subsets/

'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = [[]]
        
        def backtrack(subset, index):
            all_subsets.append(subset)
            for i in range(index+1, len(nums)):
                backtrack(subset + [nums[i]], i)
            
        for i in range(len(nums)):
            backtrack([nums[i]], i)
        
        return all_subsets
      
