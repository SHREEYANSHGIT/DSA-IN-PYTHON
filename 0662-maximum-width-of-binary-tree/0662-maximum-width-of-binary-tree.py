# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        if root is None:
            return root
        queue = deque([(root,0)])
        level = 0
        maxi = 1
        lm = float("inf")
        rm = float("-inf")

        while queue:
            level += 1
                
            lm = float("inf")
            rm = float("-inf")

            for _ in range(len(queue)):
                e,pos = queue.popleft()
                lm = min(lm,pos)
                rm = max(rm,pos)

                if e.left is not None:
                    queue.append((e.left,2*pos))
                    
                if e.right is not None:
                    queue.append((e.right,2*pos+1))
            maxi = max(maxi,rm - lm +1)

        return maxi