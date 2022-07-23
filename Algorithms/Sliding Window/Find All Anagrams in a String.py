'''

Problem 438 | Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/

'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        if len(p) <= len(s):
            l = len(p)
            to_match = {}
            for i in p:
                if i not in to_match:
                    to_match[i] = 1
                else:
                    to_match[i] += 1
            curr = {}
            for i in range(len(p)):
                if s[i] not in curr:
                    curr[s[i]] = 1
                else:
                    curr[s[i]] += 1

            if curr == to_match: 
                ans.append(0)
            
            for i in range(l, len(s)):
                if s[i] in curr:
                    curr[s[i]] += 1
                else:
                    curr[s[i]] = 1
                curr[s[i-l]] -= 1
                if curr[s[i-l]] == 0:
                    curr.pop(s[i-l])
                if curr == to_match: ans.append(i-l +1)
        return ans
      
