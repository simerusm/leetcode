from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        window = defaultdict(int)
        left_ptr = 0
        for right_ptr in range(len(s)):
            window[s[right_ptr]] += 1

            while left_ptr < right_ptr and window[s[right_ptr]] > 1:
                window[s[left_ptr]] -= 1
                if window[s[left_ptr]] == 0:
                    del window[s[left_ptr]]
                
                left_ptr += 1
                
            longest_substring = max(longest_substring, len(window))
        
        return longest_substring
