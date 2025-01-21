class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        longest = 0

        for idx, c in enumerate(s):
            if c == "(":
                stack.append(idx)
                continue
        
            stack.pop()
            if not stack:
                stack.append(idx)
            else:
                curr_length = idx - stack[-1]
                longest = max(longest, curr_length)
                
        return longest
