'''

Problem 16 | 3Sum Closest
https://leetcode.com/problems/3sum-closest/

'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        ans = 0
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                cur_diff = abs(target - total)
                if cur_diff < diff:
                    diff = cur_diff
                    ans = total
                    if diff == 0:
                        return ans
                if total < target:
                    j += 1
                else:
                    k -= 1
        return ans
       
