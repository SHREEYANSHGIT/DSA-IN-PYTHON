class Solution(object):
    def find(self,i,j,grid,path,tsum,check,d,m,n):
        self.maxi = max(self.maxi, tsum)
        for x , y in d:
            nx = i+x
            ny = j+y
            if nx >=0 and nx < m and ny < n and ny >= 0:
                if grid[nx][ny] != 0 and check[nx][ny] == False:
                    path.append(grid[nx][ny])
                    check[nx][ny] = True
                    self.find(nx,ny,grid,path,tsum + grid[nx][ny],check,d,m,n)
                    path.pop()
                    check[nx][ny] = False
        


    def getMaximumGold(self, grid):
        m = len(grid)
        n = len(grid[0])
        self.maxi = 0

        check = [[False] * n for _ in range(m)]
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    check[r][c] = True
                    self.find(r,c,grid,[grid[r][c]],grid[r][c],check,d,m,n)
                    check[r][c] = False
        return self.maxi 
            
    
        