class Solution(object):
    def dfs(self,r,c,visited,cols,rows,board):
        if r < 0 or r>= rows or c <0 or c >= cols:
            return 
        if visited[r][c] == 1:
            return
        if board[r][c] == "X":
            return 
        visited[r][c] = 1
        self.dfs(r+1, c, visited, cols, rows, board)
        self.dfs(r-1, c, visited, cols, rows, board)
        self.dfs(r, c+1, visited, cols, rows, board)
        self.dfs(r, c-1, visited, cols, rows, board)
    

    def solve(self, board):
        rows = len(board)
        cols = len(board[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        ## finding boundary zeros
        r = 0 
        c = cols-1
        for r in range(rows):
            if board[r][c] == "O" and visited[r][c] ==0:
                self.dfs(r,c,visited,cols,rows,board)
        r = 0 
        c = 0
        for r in range(rows):
            if board[r][c] == "O" and visited[r][c] == 0:
                self.dfs(r,c,visited,cols,rows,board)
        r = rows-1
        c = 0
        for c in range(cols):
            if board[r][c] == "O" and visited[r][c] == 0:
                self.dfs(r,c,visited,cols,rows,board)
        r = 0 
        c = 0
        for c in range(cols):
            if board[r][c] == "O" and visited[r][c] == 0:
                self.dfs(r,c,visited,cols,rows,board)       
        ## filling the "x" on board
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=="O" and visited[i][j]==0:
                    board[i][j] = "X"
        
        return board



        
