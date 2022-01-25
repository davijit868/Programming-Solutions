'''

Problem 90 | Subsets II
https://leetcode.com/problems/subsets-ii/

'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def backtrack(start, arr):
            if start == len(nums):
                ans.append(arr[:])
                return 
            
            backtrack(start + 1, arr + [nums[start]])
            
            while start + 1 < len(nums) and nums[start] == nums[start + 1]:
                start += 1
                
            backtrack(start + 1, arr)
                
        backtrack(0, [])
        return ans
        
