from collections import deque

class Solution(object):
    def eventualSafeNodes(self, graph):

        n = len(graph)

        reverseGraph = [[] for _ in range(n)]
        outdegree = [0] * n

        # Build reversed graph and outdegree
        for node in range(n):
            outdegree[node] = len(graph[node])
            for neighbor in graph[node]:
                reverseGraph[neighbor].append(node)

        queue = deque()

        # Terminal nodes
        for i in range(n):
            if outdegree[i] == 0:
                queue.append(i)

        result = []

        while queue:

            node = queue.popleft()
            result.append(node)

            for parent in reverseGraph[node]:

                outdegree[parent] -= 1

                if outdegree[parent] == 0:
                    queue.append(parent)

        result.sort()
        return result