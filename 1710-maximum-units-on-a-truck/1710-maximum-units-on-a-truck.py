class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key= lambda x:x[1],reverse = True)
        
        unit = 0
        y = 0
        for i , j in boxTypes:
            if truckSize < i:
                y = truckSize
            else:
                y = i
            truckSize = truckSize - y 
            unit += (y*j)
            if truckSize == 0:
                break
        return unit 

            