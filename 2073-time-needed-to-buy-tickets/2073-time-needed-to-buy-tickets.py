class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        queue = deque()

        for i in range(len(tickets)):
            queue.append(i)
            
        c = 0
        while tickets[k] > 0:
            x = queue.popleft()
            c+=1
            tickets[x]-=1
            if tickets[x] != 0:
                queue.append(x)

        
        return c 

        


            
