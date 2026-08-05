class Solution(object):
    def minimumEffortPath(self, heights):
        rows = len(heights)
        cols = len(heights[0])

        distance =[[float("inf")] * cols for _ in range(rows)]

        heap = [[0 , 0 , 0]]

        distance[0][0] = 0
        directions = [(0, 1),(0, -1),(1, 0),(-1, 0)]

        while heap :
            e , i , j =  heapq.heappop(heap)

            if i == rows -1 and j == cols - 1 :
                return distance[rows - 1][cols - 1] 

            if e > distance[i][j]:
                continue
            

            for x, y in directions:

                nr = i + x
                nc = j + y

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                
                ne = abs(heights[nr][nc] - heights[i][j])
                maxi = max(e,ne)
                if maxi < distance[nr][nc]: 
                    distance[nr][nc] = maxi
                    heapq.heappush(heap,([maxi , nr , nc]))


        return -1


