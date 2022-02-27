'''

Problem 39 | Combination Sum
https://leetcode.com/problems/combination-sum/

'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def combination(arr, idx, total):
            if total == target:
                ans.append(arr[:])
            elif total < target:
                for i in range(idx, len(candidates)):
                    combination(arr + [candidates[i]], i, total + candidates[i])
        combination([], 0, 0)
        return ans
        
        
      
