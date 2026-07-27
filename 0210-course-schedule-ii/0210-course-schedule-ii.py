class Solution(object):
    def findOrder(self, numCourses, prerequisites):

        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u] +=1

        queue = deque()
        result = []

        for i in range(0,numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            curr_node = queue.popleft()
            result.append(curr_node)
            for nb in adj[curr_node]:
                indegree[nb]-=1
                if indegree[nb]==0:
                    queue.append(nb)
            
        if len(result) == numCourses:
            return result
        return []


