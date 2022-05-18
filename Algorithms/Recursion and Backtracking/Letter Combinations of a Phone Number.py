'''

Problem 17 | Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        char_map = {2 : "abc", 3 : "def", 4 : "ghi", 5 : "jkl" , 6 : "mno", 7 : "pqrs", 8 : "tuv", 9 : "wxyz"}
        ans = []
        def backtrack(arr, idx):
            if idx == len(digits):
                ans.append("".join(arr))
                return
            for char in char_map[int(digits[idx])]:
                backtrack(arr + [char], idx + 1)
            
        if digits:
            backtrack([], 0)
        
        return ans
      
