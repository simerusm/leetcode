class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = str(num)
        for ind, c in enumerate(num_str):
            if c == '6':
                return int(num_str[:ind] + '9' + num_str[ind+1:]) if ind + 1 != len(num_str) else int(num_str[:ind] + '9')
        return int(num_str)

"""
- Greedy solution, we just replace the first 6 we see
- Loop through the number after turning it into a string, the first 6 you see replace it with a 9
- If there are no 6's, just return the number back
- Time Complexity: O(n) since we're just looping through the length of the number after turning it into a string
- Space Complexity: O(1)
"""
