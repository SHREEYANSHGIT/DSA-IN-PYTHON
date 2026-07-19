from collections import deque

class Solution(object):
    def orangesRotting(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh = 0

        # Step 1: Count fresh oranges and
        # put all rotten oranges into queue
        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 1:
                    fresh += 1

                elif grid[i][j] == 2:
                    queue.append((i, j))

        # No fresh oranges
        if fresh == 0:
            return 0

        minutes = 0

        directions = [
            (1, 0),    # Down
            (-1, 0),   # Up
            (0, 1),    # Right
            (0, -1)    # Left
        ]

        # Multi-Source BFS
        while queue:

            size = len(queue)

            for _ in range(size):

                i, j = queue.popleft()

                for di, dj in directions:

                    ni = i + di
                    nj = j + dj

                    # Boundary check
                    if 0 <= ni < rows and 0 <= nj < cols:

                        if grid[ni][nj] == 1:

                            grid[ni][nj] = 2
                            fresh -= 1

                            queue.append((ni, nj))

            # Increase minute only if
            # there are new oranges to process
            if queue:
                minutes += 1

        if fresh == 0:
            return minutes

        return -1