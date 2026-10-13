class Solution(object):
    def find(self,i,j,n,grid,d):
        if grid[i][j] == (n*n) - 1 :
            return True
        
        for x , y in d:
            nx = i + x
            ny = j + y
            if nx < n and nx >=0 and ny < n and ny >=0:
                if grid[nx][ny] == grid[i][j] + 1:
                    return self.find(nx,ny,n,grid,d)

        return False


    def checkValidGrid(self, grid):
        if grid[0][0] != 0:
            return False
        n = len(grid)
        d = [(-2, 1), (-1, 2), (1, 2), (2, 1),(2, -1), (1, -2), (-1, -2), (-2, -1)]
        return self.find(0,0,n,grid,d)