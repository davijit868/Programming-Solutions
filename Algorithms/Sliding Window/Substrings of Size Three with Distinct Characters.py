'''

Problem 1876 | Substrings of Size Three with Distinct Characters
https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

'''

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        hash_map = {}
        ans = 0
        if len(s) >= 3:
            flag = True
            for i in range(3):
                if s[i] not in hash_map.keys():
                    hash_map[s[i]] = 1
                else:
                    flag = False
                    hash_map[s[i]] += 1
            if flag: ans += 1
        for i in range(3, len(s)):
            hash_map[s[i-3]] -= 1
            if hash_map[s[i-3]] == 0: 
                hash_map.pop(s[i-3])
            if s[i] not in hash_map.keys():
                hash_map[s[i]] = 1
            else:
                hash_map[s[i]] += 1
            if len(hash_map) == 3: ans += 1
        return ans
        
