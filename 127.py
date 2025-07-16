class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        words=list("abcdefghijklmnoprstuwvxyzq")
        canGet=set(wordList)
        seen=set()
        stack=[(beginWord,1)]
        if endWord not in canGet:
            return 0
        while stack:
            word,count = stack.pop(0)
            seen.add(word)
            if word==endWord:
                return count
            for i in range(len(word)):
                for c in words:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in canGet and new_word not in seen:
                        seen.add(new_word)
                        stack.append((new_word, count + 1))

        return 0

        
