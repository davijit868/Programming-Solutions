'''

https://leetcode.com/problems/unique-binary-search-trees/

'''

class Solution:
    def numTrees(self, n: int) -> int:
        def count_trees(n):
            result = [0]*(n+1)
            result[0] = 1
            for i in range(1, n+1):
                for j in range(i):
                    result[i] += result[j]*result[i-1-j]
            return result[n]
        return count_trees(n)
      
