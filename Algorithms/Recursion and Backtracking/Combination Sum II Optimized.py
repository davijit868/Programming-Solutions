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
                ans.append(arr)
            elif total < target:
                prev = -1
                for i in range(idx, len(candidates)):
                    if candidates[i] == prev:
                        continue
                    combine(arr + [candidates[i]], i + 1, total + candidates[i])
                    prev = candidates[i]
        combine([], 0, 0)
        return ans
            
            
        
