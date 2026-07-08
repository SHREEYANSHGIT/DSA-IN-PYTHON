# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        res = []
        queue = deque([root])

        while queue:
            level = []
            levelsize = len(queue)

            for _ in range(levelsize):
                node = queue.popleft()
                level.append(node.val)
            
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
            if len(res)%2 != 0 :  ## if true means it is odd number
                level.reverse()
            
            res.append(level)
        
        return res
                

                
                
                
