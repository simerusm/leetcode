class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 97 is a, 122 is z
        # base cases
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        from collections import deque
        q = deque([(beginWord, 1)])
        seen = {beginWord}

        def isValid(word: str):
            return word not in seen and word in wordList

        while q:
            currWord, currSteps = q.popleft()
            if currWord == endWord:
                return currSteps
            
            listCurrWord = list(currWord)
            for ind, char in enumerate(listCurrWord):
                temp = listCurrWord.copy()
                for asc in range(97, 123): # get ascii of letters a-z
                    letter = chr(asc)
                    #print(letter)
                    temp[ind] = letter
                    #print("".join(temp))
                    if isValid("".join(temp)):
                        q.append(("".join(temp), currSteps + 1))
                        seen.add("".join(temp))
        return 0
