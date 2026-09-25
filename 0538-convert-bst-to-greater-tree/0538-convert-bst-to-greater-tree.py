class Solution(object):

    def dfs(self, node, s):
        if node is None:
            return s

        # Right subtree first
        s = self.dfs(node.right, s)

        # Update current node
        s += node.val
        node.val = s

        # Left subtree
        s = self.dfs(node.left, s)

        return s

    def convertBST(self, root):
        self.dfs(root, 0)
        return root