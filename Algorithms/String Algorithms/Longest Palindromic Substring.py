'''

Problem 5 | Longest Palindromic Substring | Expand Around Center
https://leetcode.com/problems/longest-palindromic-substring/

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        result_length = 0
        
        def palindrome(left, right):
            nonlocal result, result_length
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                length = right - left + 1
                if length > result_length:
                    result = s[left : right + 1]
                    result_length = length
                left -= 1
                right += 1
        
        for i in range(0, len(s)):
            palindrome(i, i)
            palindrome(i - 1, i)
            
        return result
      
