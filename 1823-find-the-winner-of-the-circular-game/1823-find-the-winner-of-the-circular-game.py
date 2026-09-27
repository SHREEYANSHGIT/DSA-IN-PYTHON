class Solution(object):
    def findTheWinner(self, n, k):
        queue = deque()
        c = 0
        for i in range(1,n+1):
            queue.append(i)
        
        while len(queue)!=1:
            x = queue.popleft()
            c += 1
            if c != k:
                queue.append(x)
            else:
                c = 0
        ans = queue.popleft()
        return ans


