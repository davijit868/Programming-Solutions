'''

Problem 567 | Permutation in String
https://leetcode.com/problems/permutation-in-string/

'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l = len(s1)
        s1_hash = {}
        for i in s1:
            if i not in s1_hash:
                s1_hash[i] = 0
            else:
                s1_hash[i] += 1
        
        look_up = {}
        for i in range(l):
            if s2[i] not in look_up:
                look_up[s2[i]] = 0
            else:
                look_up[s2[i]] += 1
                
        ans = True
        for key, val in s1_hash.items():
            if key in look_up and s1_hash[key] == look_up[key]:
                continue
            else:
                ans = False
                break
        
        if ans: return True
        
        for i in range(1, len(s2) - l + 1):
            look_up[s2[i-1]] -= 1
            if s2[i + l - 1] not in look_up:
                look_up[s2[i + l - 1]] = 0
            else:
                look_up[s2[i + l - 1]] += 1
            
            ans = True
            for key, val in s1_hash.items():
                if key in look_up and s1_hash[key] == look_up[key]:
                    continue
                else:
                    ans = False
                    break
        
            if ans: return True
          
