from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_freq = Counter(ransomNote)
        magazine_freq = Counter(magazine)

        for char, freq in ransomNote_freq.items():
            if magazine_freq[char] < freq:
                return False
        
        return True
