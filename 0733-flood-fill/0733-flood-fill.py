class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        rows = len(image)
        cols = len(image[0])

        old_color = image[sr][sc]

        if old_color == color:
            return image

        queue = deque()
        queue.append((sr,sc))
        image[sr][sc] = color

        directions = [
            (1, 0),    # Down
            (-1, 0),   # Up
            (0, 1),    # Right
            (0, -1)    # Left
        ]

        while queue:
            size = len(queue)

            for _ in range(size):
                i,j = queue.popleft()
            
                for dx , dy in directions:
                    ni = i + dx
                    nj = j + dy
                    if 0 <= ni < rows and 0 <= nj < cols:
                        if image[ni][nj] == old_color:
                            image[ni][nj] = color
                            queue.append((ni,nj))
        

        return image

            