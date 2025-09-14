class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen=set()
        ans=0
        for i in s:
            if i in seen:
                ans+=1
                seen=set()
            seen.add(i)
        return ans+1
