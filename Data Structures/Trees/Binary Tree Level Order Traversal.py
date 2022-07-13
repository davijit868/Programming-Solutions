'''

Problem 102 | Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        ans = []
        if root:
            arr.append(root)
        else:
            return []
        
        while len(arr):
            temp = []
            for i in range(len(arr)):
                curr = arr.pop(0)
                temp.append(curr.val)
                if curr.left:
                    arr.append(curr.left)
                if curr.right:
                    arr.append(curr.right)
            ans.append(temp)
        
        return ans
            
