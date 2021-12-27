'''

Problem 1002 | Find Common Characters
https://leetcode.com/problems/find-common-characters/

'''

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        lookup = [100 for i in range(26)]
        for word in words:
            new_lookup = [0 for i in range(26)]
            for char in word:
                idx = ord(char) - ord('a')
                new_lookup[idx] += 1
            lookup = [min(lookup[i], new_lookup[i]) for i in range(26)]
        answer = []
        for i in range(26):
            for j in range(lookup[i]):
                answer.append(chr(97 + i))
        return answer
        
