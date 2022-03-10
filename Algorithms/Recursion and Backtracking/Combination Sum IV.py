'''

Problem 377 | Combination Sum IV
https://leetcode.com/problems/combination-sum-iv/

'''

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ans = []
        def recursion(total, arr):
            if total == target:
                ans.append(arr[:])
            if total < target:
                for i in nums:
                    recursion(total + i, arr + [i])  
        recursion(0, [])
        return len(ans)
    
