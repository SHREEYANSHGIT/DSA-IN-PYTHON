# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        queue = deque([root])
        height = 0
        while queue:
            levelsize = len(queue)
            height +=1

            for _ in range(levelsize):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        
        
        return height