class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        ans=0
        k=0
        for i in str(num):
            if i=="9":
                ans=ans*10+9
            elif i=="6" and k==0:
                k+=1
                ans=ans*10+9
            else:
                ans=ans*10+6
        return ans
                
        
        
