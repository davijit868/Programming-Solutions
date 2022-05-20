'''

Problem 647 | Palindromic Substrings
https://leetcode.com/problems/palindromic-substrings/

'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = []
        def backtrack(arr, i):
            if arr == arr[::-1]:
                ans.append(arr)
            if i + 1 < len(s):
                backtrack(arr + s[i + 1], i + 1)
        for i in range(len(s)): 
            backtrack(s[i], i)
        
        return len(ans)
            
