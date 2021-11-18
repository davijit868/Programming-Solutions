'''

Problem 278 | First Bad Version
https://leetcode.com/problems/first-bad-version/

'''
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        r = n - 1
        l = 0
        while l <= r:
            mid = l + (r - l) // 2
            if isBadVersion(mid) == False:
                l = mid + 1
            else:
                r = mid - 1
        return l
       
