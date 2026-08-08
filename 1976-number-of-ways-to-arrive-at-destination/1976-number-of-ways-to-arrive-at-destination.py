class Solution(object):
    def countPaths(self, n, roads):

        MOD = 10**9 + 7

        # Build adjacency list
        adj = [[] for _ in range(n)]

        for u, v, time in roads:
            adj[u].append((v, time))
            adj[v].append((u, time))

        # Minimum distance to every node
        distance = [float("inf")] * n
        distance[0] = 0

        # Number of shortest ways to every node
        ways = [0] * n
        ways[0] = 1

        heap = [[0,0]]

        while heap:
            d , node = heapq.heappop(heap)

            if d > distance[node]:
                continue
            
            for nb , dist in adj[node]:
                ndist = d + dist
                if ndist == distance[nb]:
                    ways[nb] = (ways[node] + ways[nb]) % MOD
                elif ndist < distance[nb]:
                    ways[nb] = ways[node]
                    distance[nb] = ndist
                    heapq.heappush(heap,([ndist , nb]))

        return ways[n-1]
                



