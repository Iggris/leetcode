import heapq
class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        piles=[-x for x in piles]
        heapq.heapify(piles)
        for i in range(k):
            x=-1*heappop(piles)
            remove=x//2
            heappush(piles,-(x-remove))
        return -1*sum(piles)
