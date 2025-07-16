class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        words=["A","C","G","T"]
        canGet=set(bank)
        stack = [(startGene,0)]
        seen=set()
        if endGene not in canGet:
            return -1
        while stack:
            word, step= stack.pop(0)
            if word == endGene:
                return step
            seen.add(word)
            helper=list(word)
            for i in range(len(word)):
                for j in words:
                    helper[i]=j
                    x="".join(helper)
                    if x in canGet and x not in seen:
                        stack.append((x,step+1))
                helper=list(word)
                
        return -1

        
