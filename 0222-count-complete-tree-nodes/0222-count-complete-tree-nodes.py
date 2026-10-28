
class Solution(object):
    def countNodes(self, root):
        def getleftheight(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        def getrightheight(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h

        def count(root):
            if root is None:
                return 0

            lh = getleftheight(root)
            rh = getrightheight(root)

            if lh == rh:
                return 2 ** lh - 1

            return count(root.left) + count(root.right) + 1

        return count(root)
