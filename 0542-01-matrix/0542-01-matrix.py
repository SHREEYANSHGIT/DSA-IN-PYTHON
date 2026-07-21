class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(mat)
        cols = len(mat[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        distance = [[0 for _ in range(cols)] for _ in range(rows)]

        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append([i,j,0])
                    visited[i][j] = 1
        
        while queue:
            i , j , d = queue.popleft()
            distance[i][j] = d
            for x,y in [(0,-1),(0,1),(-1,0),(1,0)]:
                nr = i + x
                nc = j + y
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                if visited[nr][nc] == 1:
                    continue
                visited[nr][nc] = 1
                queue.append([nr,nc,d+1])

        return distance



                

            
                    
        

