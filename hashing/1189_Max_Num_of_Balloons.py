from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        min_instances = float('inf')
        char_freq = Counter(text)
        balloon_char_freq = Counter("balloon")

        for char, freq in balloon_char_freq.items():
            min_instances = min(min_instances, char_freq[char] // freq)
        
        return min_instances
