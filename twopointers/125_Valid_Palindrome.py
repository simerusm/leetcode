class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while l < len(s) and not s[l].isalnum():
                l += 1
            while r > 0 and not s[r].isalnum():
                r -= 1
            
            if l < len(s) and r > 0 and l < r and s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        return True
