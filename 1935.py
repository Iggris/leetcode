class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        k=len(text.split(" "))
        for i in text.split(" "):
            for j in brokenLetters:
                if j in i:
                    k-=1
                    break
        return max(k,0)
