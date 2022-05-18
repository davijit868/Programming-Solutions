'''

Problem 91 | Decode Ways
https://leetcode.com/problems/decode-ways/

'''

class Solution:
    def numDecodings(self, s: str) -> int:
        ans = []
        char_map = {'1' : 'A', '2' : 'B', '3' : 'C', '4' : 'D', '5' : 'E', '6' : 'F', '7' : 'G', '8' : 'H', '9' : 'I', '10' : 'J', '11' : 'K', '12' : 'L', \
                   '13' : 'M', '14' : 'N', '15' : 'O', '16' : 'P',  '17' : 'Q', '18' : 'R', '19' : 'S', '20' : 'T', '21' : 'U', '22' : 'V', '23' : 'W', '24' : 'X', '25' : 'Y', '26' : 'Z'}
        
        if 1 <= int(s[0]) <= 26: 
            dp = [1, 1]
            if len(s) > 1:
                for i in range(1, len(s)):
                    l1 = l2 = 0
                    if s[i] in char_map.keys():
                        l1 = dp[-1]
                    if s[i - 1 : i + 1] in char_map.keys():
                        l2 = dp[-2]
                    dp.append(l1 + l2)
            return dp[-1]
        else:
            return 0
            
