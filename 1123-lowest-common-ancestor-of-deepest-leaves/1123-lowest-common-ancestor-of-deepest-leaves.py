
class Solution(object):
    def lcaDeepestLeaves(self, root):
        def dfs(root):
            if root is None:
                return (None, 0)

            ln, lh = dfs(root.left)
            rn, rh = dfs(root.right)

            if lh == rh:
                return (root, lh + 1)

            if lh < rh:
                return (rn, rh + 1)
            else:
                return (ln, lh + 1)

        return dfs(root)[0]
