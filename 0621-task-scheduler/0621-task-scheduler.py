from collections import deque
import heapq

class Solution(object):
    def leastInterval(self, tasks, n):

        # Step 1: Frequency HashMap
        hashmap = {}

        for task in tasks:
            hashmap[task] = hashmap.get(task, 0) + 1

        # Step 2: Max Heap
        heap = []

        for task, freq in hashmap.items():
            heapq.heappush(heap, (-freq, task))

        # Step 3: Cooling Queue
        q = deque()

        time = 0

        while heap or q:

            time += 1

            if heap:

                freq, task = heapq.heappop(heap)

                # One execution completed
                freq += 1      # because freq is negative

                if freq != 0:
                    q.append((time + n, freq, task))

            # Move task back to heap after cooldown
            if q and q[0][0] == time:
                availableTime, freq, task = q.popleft()
                heapq.heappush(heap, (freq, task))

        return time