class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        lPtr = 0
        rPtr = len(s) - 1

        while lPtr < rPtr:
            leftChar = s[lPtr]
            s[lPtr] = s[rPtr]
            s[rPtr] = leftChar

            rPtr -= 1
            lPtr += 1
