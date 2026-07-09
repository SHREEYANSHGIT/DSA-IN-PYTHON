# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        if root is None:
            return []

        res = []
        

        def reversepostorder(root,level,res):
            if not root:
                return 
            if level == len(res):
                res.append(root.val)

            reversepostorder(root.right,level +1,res)
            reversepostorder(root.left,level +1,res)
        
        reversepostorder(root,0,res)
        
        return res