class Solution(object):
    def networkDelayTime(self, times, n, k):
        adj = [[] for _ in range(n+1)]

        for u , v , d in times:
            adj[u].append([v,d])

        distance = [float('inf')]*(n+1)
        distance[k] = 0
        heap = [[0,k]]

        while heap:
            dist , node = heapq.heappop(heap)

            if distance[node] < dist:
                continue
            
            for nb , d in adj[node]:
                if distance[nb] > (dist + d):
                    distance[nb] = (dist + d)
                    heapq.heappush(heap,([distance[nb] , nb]))

        for i in range(1,n+1):
            if distance[i] == float("inf"):
                return -1

        ans = distance[0]
            
        return max(distance[1:])
