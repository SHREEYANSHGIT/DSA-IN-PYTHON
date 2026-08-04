class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1 
        distance = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        queue.append((1 , 0 , 0)) # d , i , j
        distance[0][0] = 1
        while queue:
            d , i , j  = queue.popleft()
            if distance[i][j] < d:
                continue
            for x , y in [(0,1) , (0,-1) , (1,0) ,(-1,0) , (-1,-1),(1,1),(1,-1),(-1,1)]:
                nr = i + x
                nc = j + y
                if nr <0 or nr>=rows or nc < 0 or nc>= cols:
                    continue
                if grid[nr][nc] == 1:
                    continue
                if distance[nr][nc] > (d + 1):
                    distance[nr][nc] = (d+1)
                    queue.append(((d+1),nr ,nc))
        if distance[rows-1][cols-1] == float("inf") :
            return -1 
        else :
            return distance[rows-1][cols-1] 
        
            




        
        