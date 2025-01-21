class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c not in map:
                stack.append(c)
                continue
            
            if stack and stack[-1] == map[c]:
                stack.pop()
            else:
                return False
        
        return not stack
