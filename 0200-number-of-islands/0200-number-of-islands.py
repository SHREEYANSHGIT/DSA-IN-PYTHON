class Solution(object):
    def dfs(self,r, c,rows , cols , grid , visited):
        if r < 0 or r>= rows or c<0 or c>= cols:
            return
        if visited[r][c] ==1 or grid[r][c]=="0":
            return
        visited[r][c] =1
        self.dfs(r+1, c,rows , cols , grid , visited)
        self.dfs(r-1, c,rows , cols , grid , visited)
        self.dfs(r, c+1,rows , cols , grid , visited)
        self.dfs(r, c-1,rows , cols , grid , visited)
        

    def numIslands(self, grid):
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        visited = [[0 for _ in range (cols)] for _ in range(rows)]
        count = 0 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and visited[i][j] !=1:
                    count +=1
                    self.dfs(i, j,rows , cols , grid , visited)

        return count
