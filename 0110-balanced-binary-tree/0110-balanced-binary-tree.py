# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def heightmax (root):
            if root == None:
                return 0    

            leftmax = heightmax(root.left)
            if leftmax == -1:
                return -1    
            rightmax = heightmax(root.right)

            if rightmax == -1:
                return -1
            
            if abs(rightmax - leftmax) > 1 :
                return -1

            return 1 + max(leftmax,rightmax)
        
        return heightmax(root) != -1

