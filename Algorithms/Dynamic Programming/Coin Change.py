'''

https://leetcode.com/problems/coin-change/

'''

class Solution:
    def coin_change(self, coins: List[int], amount: int) -> int:
        if amount > 0:
            min_coin = [-1 for i in range(amount + 1)]
            for i in coins:
                if i < amount + 1:
                    min_coin[i] = 1
            for i in range(amount + 1):
                if min_coin[i] == -1:
                    l = []
                    for j in coins:
                        if (i - j > 0) and (min_coin[i - j] != -1):
                            l.append(min_coin[i - j] + 1)
                    if len(l):
                        min_coin[i] = min(l)
            return min_coin[-1]
        else:
            return 0
