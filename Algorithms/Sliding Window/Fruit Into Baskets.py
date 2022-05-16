'''

Problem 904 | Fruit Into Baskets
https://leetcode.com/problems/fruit-into-baskets/

'''

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        picked = {}
        total = 0
        l = 0
        for idx, val in enumerate(fruits):
            if val not in picked:
                picked[val] = 1
            else:
                picked[val] += 1
            while len(picked) > 2 and l < idx:
                picked[fruits[l]] -= 1
                if picked[fruits[l]] == 0:
                    picked.pop(fruits[l])
                l += 1
            total = max(total, sum(picked.values()))

        return total
        
