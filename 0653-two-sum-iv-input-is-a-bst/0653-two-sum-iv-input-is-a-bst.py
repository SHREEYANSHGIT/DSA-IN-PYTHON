# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        hashset = set()

        def dfs(root,k,hashset):
            if root == None:
                return 

            if k-root.val in hashset:
                return True
            
            hashset.add(root.val)

            if dfs(root.left,k,hashset):
                return True
            if dfs(root.right,k,hashset):
                return True

            return False
        
        return dfs(root,k,hashset)

             