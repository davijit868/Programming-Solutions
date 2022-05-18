'''

Problem 91 | Decode Ways
https://leetcode.com/problems/decode-ways/

'''

class Solution:
    def numDecodings(self, s: str) -> int:
        ans = []
        char_map = {'1' : 'A', '2' : 'B', '3' : 'C', '4' : 'D', '5' : 'E', '6' : 'F', '7' : 'G', '8' : 'H', '9' : 'I', '10' : 'J', '11' : 'K', '12' : 'L', \
                   '13' : 'M', '14' : 'N', '15' : 'O', '16' : 'P',  '17' : 'Q', '18' : 'R', '19' : 'S', '20' : 'T', '21' : 'U', '22' : 'V', '23' : 'W', '24' : 'X', '25' : 'Y', '26' : 'Z'}
        def recursion(processed, remain):
            if not remain:
                ans.append(processed)
                return 
            if remain[0] in char_map.keys():
                recursion(processed + char_map[remain[0]], remain[1:])
            if len(remain) >= 2 and remain[0:2] in char_map.keys():
                recursion(processed + char_map[remain[0:2]], remain[2:])
                
            
        recursion("", s)
        return len(ans)
      
