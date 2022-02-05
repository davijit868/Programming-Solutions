'''

Problem 637 | Average of Levels in Binary Tree
https://leetcode.com/problems/average-of-levels-in-binary-tree/

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue, average = [root], []
        while queue:
            total = 0
            l = len(queue)
            for i in range(l):
                cur = queue.pop(0)
                total += cur.val
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
            average.append(total/l)
        return average
        
