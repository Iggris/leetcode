class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        dic={}
        ans=0
        k=0
        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        sorted_dic=sorted(dic.items(),key=lambda x: x[1], reverse=True)
        for _,v in sorted_dic:
            if v%2==0:
                ans+=v
            else:
                if k==0:
                    ans+=v
                    k=1
                elif v-1>0 and k==1:
                    ans+=v-1

        return ans

        
