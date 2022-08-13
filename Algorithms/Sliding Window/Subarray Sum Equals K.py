'''

Problem 560 | Subarray Sum Equals K | This only will work on positive integers
https://leetcode.com/problems/subarray-sum-equals-k/

'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        i = j = 0
        temp = 0
        while j < len(nums):
            temp += nums[j]
            if temp == k:
                ans += 1
                j += 1
            elif temp < k:
                j += 1
            else:
                while temp > k:
                    if i < j:
                        temp -= nums[i]
                        i += 1
                        if temp == k:
                            ans += 1
                    else:
                        break
                j += 1
        return ans
                    
