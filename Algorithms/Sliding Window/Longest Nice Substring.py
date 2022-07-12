'''

Problem 1763 | Longest Nice Substring
https://leetcode.com/problems/longest-nice-substring/

'''

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        subs = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
        nice = [sub for sub in subs if set(sub)==set(sub.swapcase())]
        
        return max(nice, key=len, default="")
      
