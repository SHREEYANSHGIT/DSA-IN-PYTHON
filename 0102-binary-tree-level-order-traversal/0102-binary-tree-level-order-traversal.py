# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []

        def bfs(root):
            res = []
            queue = deque([root])

            while queue:
                levelsize = len(queue)
                level = []

                for _ in range(levelsize):
                    node = queue.popleft()
                    level.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    
                res.append(level)

            
            return res
        return bfs(root)



        

                

        
        