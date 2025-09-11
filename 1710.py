class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        ans=0
        boxTypes.sort(key = lambda x: x[1], reverse=True)
        for i,j in boxTypes:
            if i<=truckSize:
                ans+=i*j
                truckSize-=i
            else:
                ans+=truckSize*j
                truckSize=0
            if truckSize==0:
                break
        return ans
