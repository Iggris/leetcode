class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        ans=0
        while target!=1:
            if target%2==0 and maxDoubles>0:
                target//=2
                maxDoubles-=1
                ans+=1
            else:
                target-=1
                ans+=1
            if maxDoubles==0:
                ans=ans+target-1
                break
        return ans
