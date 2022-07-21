'''

Problem 239 | Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/

'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        ans = []
        for i in range(k):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)

        for i in range(k, len(nums)):
            ans.append(nums[queue[0]])
            while queue and queue[0] <= (i-k):
                queue.popleft()
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        ans.append(nums[queue[0]])
        
        return ans
      
