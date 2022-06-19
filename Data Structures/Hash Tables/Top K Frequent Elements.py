'''

Problem 347 | Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        for n, c in count.items():
            freq[c].append(n)
            
        res = []
        for i in range(len(freq) -1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
                    
