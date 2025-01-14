from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_freq = Counter(stones)
        total_jewel_stones = 0

        for char in jewels:
            total_jewel_stones += stones_freq[char]
        
        return total_jewel_stones
