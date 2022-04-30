'''

Problem 216 | Combination Sum III
https://leetcode.com/problems/combination-sum-iii/

'''

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backtrack(arr, total):
            if len(arr) == k and total == n:
                ans.append(arr)
            if total < n:
                start = arr[-1] if len(arr) > 0 else 0
                for i in range(start + 1, 10):
                    backtrack(arr + [i], total + i)
 
        backtrack([], 0)
        return ans
  
