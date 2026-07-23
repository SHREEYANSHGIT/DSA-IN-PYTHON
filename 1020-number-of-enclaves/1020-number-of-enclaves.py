class Solution(object):

    def numEnclaves(self, grid):

        if not grid:
            return

        rows = len(grid)
        cols = len(grid[0])

        visited = [[0] * cols for _ in range(rows)]
        queue = deque()

        # Left boundary
        for r in range(rows):
            if grid[r][0] == 1 and not visited[r][0]:
                visited[r][0] =1
                queue.append((r,0))

        # Right boundary
        for r in range(rows):
            if grid[r][cols - 1] == 1 and not visited[r][cols - 1]:
                visited[r][cols - 1] =1
                queue.append((r,cols - 1))

        # Top boundary
        for c in range(cols):
            if grid[0][c] == 1 and not visited[0][c]:
                visited[0][c] =1
                queue.append((0,c))

        # Bottom boundary
        for c in range(cols):
            if grid[rows - 1][c] == 1 and not visited[rows - 1][c]:
                visited[rows - 1][c] =1
                queue.append((rows - 1,c))
        
        while queue:
            i , j = queue.popleft()
            
            for x, y in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr = i + x
                nc = j + y
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                if grid[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc]=1
                    queue.append((nr,nc))




        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    grid[i][j] = 1
                    count+=1
        
        return count 
