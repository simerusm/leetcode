class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        def backtrack(l: int, r: int, deletions: bool = True) -> bool:
            if not l < r:
                return True
            
            if s[l] == s[r]:
                return backtrack(l + 1, r - 1, deletions)
            else:
                first, second = False, False

                if deletions and s[l] == s[r - 1]:
                    first = backtrack(l + 1, r - 2, False)
                
                if deletions and s[l + 1] == s[r] and not first:
                    second = backtrack(l + 2, r - 1, False)
                
                return first or second

        return backtrack(l, r)
