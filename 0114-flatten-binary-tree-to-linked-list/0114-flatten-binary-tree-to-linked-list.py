# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        self.nextright = None
        def revpreorder(root):
            if root == None:
                return 
            
            revpreorder(root.right)
            revpreorder(root.left)

            root.left = None
            root.right = self.nextright
            self.nextright = root
        
        revpreorder(root)
        return self.nextright

            
