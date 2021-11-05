'''

https://leetcode.com/problems/arranging-coins/

'''

class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        count = 0
        while(True):
            n = n - i
            i += 1
            if n < 0:
                break
            count += 1
        return count
      
