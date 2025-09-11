class Solution(object):
    def maxNumberOfApples(self, weight):
        """
        :type weight: List[int]
        :rtype: int
        """
        weight.sort()
        ans=0
        bucket=5000
        for i in weight:
            if i>bucket:
                return ans
            ans+=1
            bucket-=i
        return ans
