class Solution(object):
    def find(self, i, n, grid, arr, ans):
        if i == n:
            ans.append(["".join(row) for row in grid])
            return

        for j in range(n):
            if arr[j] == 0:
                safe = True

                # Check upper-left diagonal
                r, c = i - 1, j - 1
                while r >= 0 and c >= 0:
                    if grid[r][c] == "Q":
                        safe = False
                        break
                    r -= 1
                    c -= 1

                # Check upper-right diagonal
                r, c = i - 1, j + 1
                while r >= 0 and c < n:
                    if grid[r][c] == "Q":
                        safe = False
                        break
                    r -= 1
                    c += 1

                if not safe:
                    continue

                # Place queen
                grid[i][j] = "Q"
                arr[j] = 1

                self.find(i + 1, n, grid, arr, ans)

                # Backtrack
                grid[i][j] = "."
                arr[j] = 0

    def solveNQueens(self, n):
        grid = [["." for _ in range(n)] for _ in range(n)]
        arr = [0] * n
        ans = []

        self.find(0, n, grid, arr, ans)
        return ans