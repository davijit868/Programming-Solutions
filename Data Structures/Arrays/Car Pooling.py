'''

Problem 1094 | Car Pooling
https://leetcode.com/problems/car-pooling/

'''

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_len = 1000
        seat = [0 for i in range(max_len)]
        for trip in trips:
            for i in range(trip[1], trip[2]):
                seat[i] += trip[0]
        
        for i in seat:
            if i > capacity:
                return False
        return True
        
