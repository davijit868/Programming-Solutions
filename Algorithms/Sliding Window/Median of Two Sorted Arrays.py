'''

Problem 4 | Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/

'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans = []
        i = j = 0
        
        l1 = len(nums1)
        l2 = len(nums2)
        
        even = False
        
        if (l1 + l2) % 2 == 0:
            even = True
        m = (l1 + l2) // 2
            
        
        while i < l1 and j < l2:
            if nums1[i] < nums2[j]:
                ans.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                ans.append(nums2[j])
                j += 1
            else:
                ans.append(nums1[i])
                ans.append(nums2[j])
                j += 1
                i += 1
       
        
        while i < l1:
            ans.append(nums1[i])
            i += 1
        while j < l2:
            ans.append(nums2[j])
            j += 1
        
        if even:
            return (ans[m] + ans[m-1]) / 2
        else:
            return ans[m]
        
        
