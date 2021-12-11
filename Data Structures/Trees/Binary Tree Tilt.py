'''

Problem 563 | Binary Tree Tilt
https://leetcode.com/problems/binary-tree-tilt/

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total_tilt = 0
        def sum_at_node(node):
            nonlocal total_tilt
            if not node:
                return 0
            left_sum = sum_at_node(node.left)
            right_sum = sum_at_node(node.right)
            total_tilt += abs(left_sum - right_sum)
            return node.val + left_sum + right_sum 
        sum_at_node(root)
        return total_tilt
        
