# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isCousins(self, root, x, y):

        if not root:
            return 0

        queue = deque([(root, 0)])
        level = 0
        a =None
        b = None
        while queue:
            level += 1

            for _ in range(len(queue)):
                node, p = queue.popleft()
                if node.val == x :
                    a = (x,level,p)
                if node.val == y :
                    b = (y,level,p)

                if node.left:
                    queue.append((node.left, node))

                if node.right:
                    queue.append((node.right, node))
                    
            if not a and b:
                return False
            if not a and b:
                return False
            if a and b:
                if a[1] != b[1] or a[2] == b[2]:
                    return False
                elif a[1] == b[1] and a[2] != b[2]:
                    return True

        return False