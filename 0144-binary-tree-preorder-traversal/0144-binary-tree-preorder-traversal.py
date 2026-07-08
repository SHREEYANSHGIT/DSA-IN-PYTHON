# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        rest = []
        def preorder(node,rest):
            if node == None:
                return 
            rest.append(node.val)
            preorder(node.left,rest)
            preorder(node.right,rest)
        
        preorder(root,rest)
        return rest