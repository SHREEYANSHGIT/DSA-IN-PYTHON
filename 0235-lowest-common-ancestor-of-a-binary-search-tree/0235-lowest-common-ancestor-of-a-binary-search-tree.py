
class Solution(object):
    def dfs(self, root, p, q):
        if min(p.val, q.val) <= root.val <= max(p.val, q.val):
            return root

        elif root.val > p.val and root.val > q.val:
            return self.dfs(root.left, p, q)

        else:
            return self.dfs(root.right, p, q)

    def lowestCommonAncestor(self, root, p, q):
        return self.dfs(root, p, q)
