'''

Problem 560 | Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        prefix = {0 : 1}
        for n in nums:
            cur_sum += n
            diff = cur_sum - k
            res += prefix.get(diff, 0)
            prefix[cur_sum] = 1 + prefix.get(cur_sum, 0)
        return res
