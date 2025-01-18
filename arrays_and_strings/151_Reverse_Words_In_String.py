class Solution:
    def reverseWords(self, s: str) -> str:
        words = []

        currWord = ""
        for c in s:
            if c == ' ':
                if currWord == "":
                    continue
                words.append(currWord)
                currWord = ""
            else:
                currWord += c
        
        if currWord != "":
            words.append(currWord)
        
        words.reverse()
        return " ".join(words)
