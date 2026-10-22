
from collections import deque

class Solution(object):
    def dfs(self, root, hm, target):
        if root is None:
            return

        if root.val == target.val:
            self.t = root

        if root.left is not None:
            hm[root.left] = root
            self.dfs(root.left, hm, target)

        if root.right is not None:
            hm[root.right] = root
            self.dfs(root.right, hm, target)

    def distanceK(self, root, target, k):
        hm = {}
        self.t = None

        self.dfs(root, hm, target)

        queue = deque([self.t])
        visited = {self.t}
        level = 0

        while queue:
            if level == k:
                return [node.val for node in queue]

            for _ in range(len(queue)):
                e = queue.popleft()

                if e.left and e.left not in visited:
                    visited.add(e.left)
                    queue.append(e.left)

                if e.right and e.right not in visited:
                    visited.add(e.right)
                    queue.append(e.right)

                if e in hm and hm[e] not in visited:
                    parent = hm[e]
                    visited.add(parent)
                    queue.append(parent)

            level += 1

        return []
