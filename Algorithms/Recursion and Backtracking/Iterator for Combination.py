'''

Problem 1286 | Iterator for Combination
https://leetcode.com/problems/iterator-for-combination/

'''

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        
        def backtrack(combination, i):
            if len(combination) == combinationLength:
                print(combination)
                self.combinations.append(combination)
            elif len(combination) < combinationLength:
                for j in range(i+1, len(characters)):
                    backtrack(combination+characters[j], j)
            
        for i in range(len(characters)):
            backtrack(characters[i], i)

    def next(self) -> str:
        if self.combinations:
            return self.combinations.pop(0)

    def hasNext(self) -> bool:
        if self.combinations:
            return True
        return False
      
# Your CombinationIterator object will be instantiated and called as such:
obj = CombinationIterator(characters, combinationLength)
param_1 = obj.next()
param_2 = obj.hasNext()
 
