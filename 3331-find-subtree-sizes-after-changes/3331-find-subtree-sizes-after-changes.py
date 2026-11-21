
class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)

        # Build the original tree
        tree = [[] for _ in range(n)]

        for i in range(1, n):
            tree[parent[i]].append(i)

        ans = [1] * n
        last = [-1] * 26
        prev = [-1] * n

        stack = [(0, 0, -1)]

        while stack:
            node, state, old = stack.pop()
            idx = ord(s[node]) - ord('a')

            if state == 0:
                # Enter node
                prev[node] = last[idx]
                last[idx] = node

                # Exit node after processing children
                stack.append((node, 1, old))

                for child in reversed(tree[node]):
                    stack.append((child, 0, -1))

            else:
                # Exit node: restore previous character ancestor
                last[idx] = prev[node]

                # Find the final parent
                p = prev[node] if prev[node] != -1 else parent[node]

                if p != -1:
                    ans[p] += ans[node]

        return ans
