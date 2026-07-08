# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def maxDepth(root):
            if root==None:
                return 0
            leftmax = maxDepth(root.left)
            rightmax = maxDepth(root.right)
            self.diameter = max(self.diameter,leftmax + rightmax)
            return 1+max(leftmax,rightmax)
        maxDepth(root)
        return self.diameter