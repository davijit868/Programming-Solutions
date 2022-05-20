'''

Problem 647 | Palindromic Substrings
https://leetcode.com/problems/palindromic-substrings/

'''

class Solution:
    def countSubstrings(self, s: str) -> int:    
        ans = 0
        for i in range(len(s)):
            l = r = i
            ans += 1
            while l - 1 >= 0 and r + 1 < len(s):
                if s[l - 1] == s[r + 1]:
                    ans += 1
                    l -= 1
                    r += 1
                else:
                    break
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                l = i 
                r = i + 1
                ans += 1
                while l - 1 >= 0 and r + 1 < len(s):
                    if s[l - 1] == s[r + 1]:
                        ans += 1
                        l -= 1
                        r += 1
                    else:
                        break
        return ans                    
        
