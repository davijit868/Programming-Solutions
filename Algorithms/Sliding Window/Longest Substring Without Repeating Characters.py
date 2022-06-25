'''

Problem 3 | Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        look_up = {}
        l, r = 0, 0
        ans = 0
        while r < len(s):
            
            if s[r] not in look_up:
                look_up[s[r]] = 1
                temp = (r + 1 - l)
                ans = max(ans, temp)
                r += 1
            else:
                if l <= r:
                    look_up[s[l]] -= 1
                    if look_up[s[l]] == 0:
                        look_up.pop(s[l])
                    l += 1
                else:
                    r += 1
        return ans
      
