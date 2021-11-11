'''

Problem 1178 | Naive Pythonic Solution
https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

'''

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        answer = []
        for puzzle in puzzles:
            count = 0
            for word in words:
                if puzzle[0] not in word:
                    continue
                flag = False
                for letter in set(word):
                    if letter not in puzzle:
                        flag = True
                        break
                if not flag:
                    count += 1
            answer.append(count)
        return answer
        
