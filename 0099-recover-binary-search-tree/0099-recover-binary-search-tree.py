
class Solution(object):
    def recoverTree(self, root):
        self.prev = None
        self.first = None
        self.sec = None

        def inorder(node):
            if node is None:
                return

            inorder(node.left)

            if self.prev and node.val < self.prev.val:
                if self.first is None:
                    self.first = self.prev
                self.sec = node

            self.prev = node

            inorder(node.right)

        inorder(root)

        self.first.val, self.sec.val = self.sec.val, self.first.val
