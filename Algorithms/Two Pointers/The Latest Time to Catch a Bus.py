'''

Problem 2332 | The Latest Time to Catch a Bus
https://leetcode.com/problems/the-latest-time-to-catch-a-bus/

'''

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()  
        
        i = j = cap = 0
        while i < len(buses):
            cap = capacity
            while cap and j < len(passengers) and passengers[j] <= buses[i]:
                cap -= 1
                j += 1
            i += 1
        i -= 1
        j -= 1
        
        if cap and passengers[j] != buses[i]:
            return buses[i]
        while j > 0 and passengers[j] - 1 == passengers[j - 1]:
            j -= 1
        return passengers[j] - 1
        
