# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if root is None:
            return []

        q = deque([root])
        ans = []

        while q:
            level = []
            size = len(q)

            for _ in range(size):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            ans.append(level[-1])

        return ans