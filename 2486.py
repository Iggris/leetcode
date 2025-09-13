class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        j=0
        for i in s: 
            if j<len(t) and t[j]==i:
                j+=1
        return len(t)-j 
        
