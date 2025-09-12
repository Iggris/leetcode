class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=len(arr)
        dic={}
        ans=0
        for i in arr:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        sorted_dic=sorted(dic.items(), key=lambda x: x[1],reverse=True)
        for i,j in sorted_dic:
            n-=j
            ans+=1
            if n<=len(arr)//2:
                return ans

        return ans
