'''

Problem 113 | Path Sum II
https://leetcode.com/problems/path-sum-ii/

'''

Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def depth_first_search(node, arr, total):
            if not node.left and not node.right:
                if total == targetSum:
                    ans.append(arr)
                return 
            if node.left:
                depth_first_search(node.left, arr + [node.left.val], total + node.left.val)
            if node.right:
                depth_first_search(node.right, arr + [node.right.val], total + node.right.val)
            
        if root:
            depth_first_search(root, [root.val], root.val)
       
        return ans
            
