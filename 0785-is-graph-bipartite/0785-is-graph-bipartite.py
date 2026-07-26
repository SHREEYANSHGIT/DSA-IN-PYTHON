from collections import deque

class Solution(object):
    def isBipartite(self, graph):

        V = len(graph)
        visited = [0] * V

        for i in range(V):

            if visited[i] != 0:
                continue

            queue = deque()
            queue.append(i)
            visited[i] = "r"

            while queue:

                node = queue.popleft()

                for nb in graph[node]:

                    if visited[nb] == "r" and visited[node] == "r":
                        return False

                    if visited[nb] == "b" and visited[node] == "b":
                        return False

                    if visited[nb] == 0:

                        if visited[node] == "r":
                            visited[nb] = "b"
                        else:
                            visited[nb] = "r"

                        queue.append(nb)

        return True