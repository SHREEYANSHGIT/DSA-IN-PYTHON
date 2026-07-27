class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u] +=1

        queue = deque()
        counter = 0

        for i in range(0,numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            curr_node = queue.popleft()
            counter+=1
            for nb in adj[curr_node]:
                indegree[nb]-=1
                if indegree[nb]==0:
                    queue.append(nb)
            
        if counter == numCourses:
            return True
        return False


