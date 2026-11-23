
class ProductOfNumbers(object):

    def __init__(self):
        self.prefix = []

    def add(self, num):
        if num == 0:
            self.prefix = []
        else:
            if not self.prefix:
                self.prefix.append(num)
            else:
                self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k):
        if len(self.prefix) < k:
            return 0

        n = len(self.prefix)

        if n == k:
            return self.prefix[-1]

        return self.prefix[-1] // self.prefix[n-k-1]
