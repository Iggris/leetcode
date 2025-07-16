import heapq
class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        costs=0
        heapq.heapify(sticks)
        if len(sticks)==1:
            return 0
        while len(sticks)!=1:
            x=heappop(sticks)
            y=heappop(sticks)
            costs+=x+y
            heappush(sticks,x+y)

        return costs
