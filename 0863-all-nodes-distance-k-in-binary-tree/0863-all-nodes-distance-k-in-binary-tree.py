
from collections import deque

class Solution(object):
    def dfs(self, root, hm, target):
        if root is None:
            return

        if root == target:
            self.t = root

        if root.left is not None:
            hm[root.left.val] = root
            self.dfs(root.left, hm, target)

        if root.right is not None:
            hm[root.right.val] = root
            self.dfs(root.right, hm, target)

    def distanceK(self, root, target, k):
        hm = {}
        self.t = None
        self.dfs(root, hm, target)

        visited = [False] * 501
        queue = deque([self.t])
        visited[self.t.val] = True
        level = 0

        while queue:
            if level == k:
                return [node.val for node in queue]

            size = len(queue)

            for _ in range(size):
                e = queue.popleft()

                if e.left and not visited[e.left.val]:
                    visited[e.left.val] = True
                    queue.append(e.left)

                if e.right and not visited[e.right.val]:
                    visited[e.right.val] = True
                    queue.append(e.right)

                if e.val in hm:
                    parent = hm[e.val]
                    if not visited[parent.val]:
                        visited[parent.val] = True
                        queue.append(parent)

            level += 1

        return []
