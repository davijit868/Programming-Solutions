'''

Problem 40 | Combination Sum II
https://leetcode.com/problems/combination-sum-ii/

'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def combine(arr, idx, total):
            if total == target:
                if arr not in ans:
                    ans.append(arr)
            elif total < target and idx < len(candidates):
                combine(arr + [candidates[idx]], idx + 1, total + candidates[idx])
                combine(arr, idx + 1, total)
        combine([], 0, 0)
        return ans
            
            
        
