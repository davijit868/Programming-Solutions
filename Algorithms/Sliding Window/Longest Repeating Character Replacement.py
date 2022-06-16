'''

Problem 424 | Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/

'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        look_up = {}
        output = 0
        look_up[s[r]] = 1
        while l <= r and r < len(s):
            cur_max, total = 0, 0
            for key, value in look_up.items():
                if value > cur_max:
                    cur_max = value
                total += value
            if total - cur_max <= k:
                r += 1
                if  r < len(s):
                    if s[r] not in look_up:
                        look_up[s[r]] = 1
                    else:
                        look_up[s[r]] += 1
                
                if total > output:
                    output = total
            else:
                look_up[s[l]] -= 1
                l +=1 
            
        return output
            
            
