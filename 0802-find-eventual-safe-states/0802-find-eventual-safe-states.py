class Solution(object):
    def dfs(self,curr_node,visited,path_visited,safe,v,graph):
        visited[curr_node]=1
        path_visited[curr_node]=1
        for nb in graph[curr_node]:
            if visited[nb]==0:
                ans = self.dfs(nb,visited,path_visited,safe,v,graph)
                if ans == False:
                    return False
            if path_visited[nb] == 1:
                return False
        safe[curr_node] = 1
        path_visited[curr_node]=0
        return True

    def eventualSafeNodes(self, graph):
        v = len(graph)
        visited = [0]*v
        path_visited = [0]*v
        safe = [0]*v

        for i in range(v):
            if visited[i] == 0:
                self.dfs(i,visited,path_visited,safe,v,graph)

        result = []
        for i in range(v):
            if safe[i]==1:
                result.append(i)
        return result

        
        

        