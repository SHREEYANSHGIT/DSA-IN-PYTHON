class Solution(object):
    def isBipartite(self, graph):
        V = len(graph)
        visited = [0]*V
        for i in range(V):
            if visited[i]==0:
                queue = deque()
                queue.append(i)
                visited[i] = "r"

                while queue:
                    node = queue.popleft()
                    for nb in graph[node]:
                        if visited[nb] == visited[node]:
                            return False
                        elif visited[node]=="r" and visited[nb] == 0:
                            visited[nb]="b"
                            queue.append(nb)
                        elif visited[node]=="b" and visited[nb] == 0:
                            visited[nb]="r"
                            queue.append(nb)
                
        return True


