class StockSpanner(object):

    def __init__(self):
        self.st = []

    def next(self, price):
        
        spann = 1 
        while self.st and price >= self.st[-1][0]:
            spann = spann + self.st[-1][1]
            self.st.pop()
        self.st.append((price,spann))
        return spann
            
        
