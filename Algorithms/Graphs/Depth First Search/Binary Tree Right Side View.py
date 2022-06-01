'''

Problem 199 | Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        ans = []
        if root:
            output.append(root)
            while output:
                l = len(output)
                temp = []
                for i in range(l):
                    cur = output.pop(0)
                    temp.append(cur.val)
                    if cur.left:
                        output.append(cur.left)
                    if cur.right:
                        output.append(cur.right)
                if temp:
                    ans.append(temp[-1])
        return ans
      
