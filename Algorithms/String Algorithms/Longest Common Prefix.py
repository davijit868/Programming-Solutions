'''

https://leetcode.com/problems/longest-common-prefix/

'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        i = 0
        while(True):
            if i < len(strs[0]):
                c = strs[0][i]
            else:
                break
            flag = True
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != c:
                    flag = False
                    break
            if flag:
                common += c
            else:
                break
            i += 1
        return common
            
