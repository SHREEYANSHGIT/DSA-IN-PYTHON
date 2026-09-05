class Solution(object):
    def totalFruit(self, fruits):
        maxi = 0
        hashmap = {}
        l = 0
        r = 0

        while r<len(fruits):
            hashmap[fruits[r]] = hashmap.get(fruits[r],0)+1

            if len(hashmap) > 2:
                if hashmap[fruits[l]] == 1:
                    del hashmap[fruits[l]]
                else:
                    hashmap[fruits[l]] -=1
                l = l +1
            
            maxi = max(maxi,r-l+1)

            r = r+1

        return maxi                  



