'''

https://leetcode.com/problems/single-number-iii/


'''

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        look_up = {}
        for i in nums:
            if i not in look_up.keys():
                look_up[i] = 1
            else:
                look_up[i] += 1
        answer = []
        for key, value in look_up.items():
            if look_up[key] == 1:
                answer.append(key)
        return answer
        
