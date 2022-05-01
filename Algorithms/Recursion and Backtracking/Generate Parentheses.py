'''

Problem 22 | Generate Parentheses
https://leetcode.com/problems/generate-parentheses/

'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtrack(arr, begin, end):
            if begin == n and end == n:
                ans.append(arr)
                return
            if begin <= n and end <= n:
                backtrack(arr + '(', begin + 1 , end)
                if end < begin:
                    backtrack(arr + ')', begin, end + 1)
            
        backtrack('(', 1, 0)
        return ans
      
