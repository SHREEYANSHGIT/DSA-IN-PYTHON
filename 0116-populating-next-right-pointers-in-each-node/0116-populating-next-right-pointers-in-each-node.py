class Solution(object):
    def connect(self, root):
        if root is None:
            return root

        leftmost = root

        while leftmost.left:
            current = leftmost

            while current:
                current.left.next = current.right

                if current.next:
                    current.right.next = current.next.left

                current = current.next

            leftmost = leftmost.left

        return root