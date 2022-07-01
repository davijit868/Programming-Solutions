'''

Problem 437 | Path Sum III
https://leetcode.com/problems/path-sum-iii/

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def find_sum(node, target):
            count = 0 
            if not node:
                return 0
            if node.val == target:
                count += 1
            return find_sum(node.left, target - node.val) + find_sum(node.right, target - node.val) + count
        
        def recursion(node, target):
            if not node:
                return 0
            return recursion(node.left, target) + recursion(node.right, target) + find_sum(node, target)
        
        return recursion(root, targetSum)
                
            
