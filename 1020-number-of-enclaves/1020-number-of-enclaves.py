class Solution(object):
    

    def dfs(self, r, c, visited, cols, rows, grid):

        if r < 0 or r >= rows or c < 0 or c >= cols:
            return

        if visited[r][c]:
            return

        if grid[r][c] == 0:
            return

        visited[r][c] = 1

        self.dfs(r + 1, c, visited, cols, rows, grid)
        self.dfs(r - 1, c, visited, cols, rows, grid)
        self.dfs(r, c + 1, visited, cols, rows, grid)
        self.dfs(r, c - 1, visited, cols, rows, grid)

    def numEnclaves(self, grid):

        if not grid:
            return

        rows = len(grid)
        cols = len(grid[0])

        visited = [[0] * cols for _ in range(rows)]

        # Left boundary
        for r in range(rows):
            if grid[r][0] == 1 and not visited[r][0]:
                self.dfs(r, 0, visited, cols, rows, grid)

        # Right boundary
        for r in range(rows):
            if grid[r][cols - 1] == 1 and not visited[r][cols - 1]:
                self.dfs(r, cols - 1, visited, cols, rows, grid)

        # Top boundary
        for c in range(cols):
            if grid[0][c] == 1 and not visited[0][c]:
                self.dfs(0, c, visited, cols, rows, grid)

        # Bottom boundary
        for c in range(cols):
            if grid[rows - 1][c] == 1 and not visited[rows - 1][c]:
                self.dfs(rows - 1, c, visited, cols, rows, grid)
        
        count = 0

        # Flip surrounded regions
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    grid[i][j] = 1
                    count+=1
        
        return count 
