import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap=[]
        for x,y in points:
            heapq.heappush(heap,(-(x**2+y**2),[x,y]))
            if len(heap)>k:
                heapq.heappop(heap)
        return [points[1] for points in heap]

        
