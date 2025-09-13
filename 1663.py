class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        alphabet="abcdefghijklmonupqrstuwyvzx"
        helper=[""]*27
        ans=[]
        for i in alphabet:
            helper[ord(i)-96]=i
        while n>0:
            if k>27 and k-26>=n:
                ans.append("z")
                n-=1
                k-=(ord("z")-96)
            else:
                ans.append("a"*(n-1))
                ans.append(helper[k-(n-1)])
                n=0
        ans.sort()
        return "".join(ans)
