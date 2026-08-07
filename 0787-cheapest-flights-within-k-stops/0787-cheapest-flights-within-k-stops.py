import heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):

        adj = [[] for _ in range(n)]

        for u, v, price in flights:
            adj[u].append((v, price))

        # At most k stops means at most k+1 flights
        max_flights = k + 1

        queue =deque()        
        queue.append((0, src, 0))

        # Best number of flights used when reaching each node
        distance = [float("inf")] * n
        distance [src] = 0

        while queue:

            kth, node, cost = queue.popleft()
    

            if kth >= max_flights:
                continue

            for nb, price in adj[node]:

                new_cost = cost + price
                nkth = kth + 1

                if new_cost < distance[nb]:

                    distance[nb] = new_cost

                    queue.append((nkth, nb, new_cost))
        if distance[dst]!= float("inf"):
            return distance[dst]
        return -1